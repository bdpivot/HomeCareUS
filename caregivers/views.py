from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from .models import (
    Caregiver, Certification, Experience, CaregiverStateLicense, 
    Agency, AgencyStateLicense, AuditLog, State, CertificationType, User
)
from .forms import (
    CaregiverForm, CertificationForm, ExperienceForm, 
    AgencyForm, AgencyStateLicenseForm, CaregiverFilterForm,
    CaregiverStateLicenseForm, LoginForm, RegisterForm, ResumeUploadForm
)
from .services import ResumeParserService
import PyPDF2
import docx

class AgencyRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'agency')

class AgencyDashboardView(LoginRequiredMixin, AgencyRequiredMixin, ListView):
    model = Caregiver
    template_name = 'caregivers/agency/dashboard.html'
    context_object_name = 'caregivers'

    def get_queryset(self):
        return Caregiver.objects.filter(agency=self.request.user.agency)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agency = self.request.user.agency
        context['agency'] = agency
        context['total_caregivers'] = self.get_queryset().count()
        context['active_caregivers'] = self.get_queryset().filter(status='active').count()
        context['pending_caregivers'] = self.get_queryset().filter(status='pending').count()
        context['expiring_certifications'] = Certification.objects.filter(
            caregiver__agency=agency,
            expiry_date__lte=timezone.now().date() + timedelta(days=30)
        ).count()
        context['expiring_licenses'] = CaregiverStateLicense.objects.filter(
            caregiver__agency=agency,
            expiry_date__lte=timezone.now().date() + timedelta(days=30)
        ).count()
        context['compliance_status'] = self.get_compliance_status()
        return context

    def get_compliance_status(self):
        agency = self.request.user.agency
        status = {
            'hipaa_compliance': agency.hipaa_compliance_date is not None,
            'state_licenses': AgencyStateLicense.objects.filter(agency=agency, is_active=True).exists(),
            'caregiver_compliance': self.get_queryset().filter(hipaa_compliance_status=True).count() / self.get_queryset().count() if self.get_queryset().exists() else 0,
        }
        return status

class AgencyCaregiverListView(LoginRequiredMixin, AgencyRequiredMixin, ListView):
    model = Caregiver
    template_name = 'caregivers/agency/caregiver_list.html'
    context_object_name = 'caregivers'

    def get_queryset(self):
        queryset = Caregiver.objects.filter(agency=self.request.user.agency)
        search_query = self.request.GET.get('search')
        status_filter = self.request.GET.get('status')
        state_filter = self.request.GET.get('state')
        certification_filter = self.request.GET.get('certification')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(specialties__icontains=search_query)
            )

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        if state_filter:
            queryset = queryset.filter(states_licensed__code=state_filter)

        if certification_filter:
            queryset = queryset.filter(certifications__cert_type_id=certification_filter)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agency'] = self.request.user.agency
        context['states'] = State.objects.all()
        context['certification_types'] = CertificationType.objects.all()
        return context

class AgencyCaregiverDetailView(LoginRequiredMixin, AgencyRequiredMixin, DetailView):
    model = Caregiver
    template_name = 'caregivers/agency/caregiver_detail.html'
    context_object_name = 'caregiver'

    def get_queryset(self):
        return Caregiver.objects.filter(agency=self.request.user.agency)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agency'] = self.request.user.agency
        context['certifications'] = self.object.certifications.all()
        context['experiences'] = self.object.experiences.all()
        context['state_licenses'] = self.object.caregiverstatelicense_set.all()
        context['compliance_status'] = self.get_compliance_status()
        return context

    def get_compliance_status(self):
        caregiver = self.object
        status = {
            'hipaa_compliance': caregiver.hipaa_compliance_status,
            'certifications': all(cert.is_valid() for cert in caregiver.certifications.all()),
            'state_licenses': all(license.is_valid() for license in caregiver.caregiverstatelicense_set.all()),
            'background_check': self.check_background_check(),
            'drug_test': self.check_drug_test(),
            'physical_exam': self.check_physical_exam(),
        }
        return status

    def check_background_check(self):
        # Implement background check validation logic
        return True

    def check_drug_test(self):
        # Implement drug test validation logic
        return True

    def check_physical_exam(self):
        # Implement physical exam validation logic
        return True

class AgencyCaregiverCreateView(LoginRequiredMixin, AgencyRequiredMixin, CreateView):
    model = Caregiver
    form_class = CaregiverForm
    template_name = 'caregivers/agency/caregiver_form.html'
    success_url = reverse_lazy('agency_caregiver_list')

    def form_valid(self, form):
        form.instance.agency = self.request.user.agency
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        AuditLog.objects.create(
            user=self.request.user,
            action='create',
            model_name='Caregiver',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT')
        )
        return response

class AgencyCaregiverUpdateView(LoginRequiredMixin, AgencyRequiredMixin, UpdateView):
    model = Caregiver
    form_class = CaregiverForm
    template_name = 'caregivers/agency/caregiver_form.html'
    success_url = reverse_lazy('agency_caregiver_list')

    def get_queryset(self):
        return Caregiver.objects.filter(agency=self.request.user.agency)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        response = super().form_valid(form)
        AuditLog.objects.create(
            user=self.request.user,
            action='update',
            model_name='Caregiver',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            changes=form.changed_data
        )
        return response

class AgencyCaregiverDeleteView(LoginRequiredMixin, AgencyRequiredMixin, DeleteView):
    model = Caregiver
    template_name = 'caregivers/agency/caregiver_confirm_delete.html'
    success_url = reverse_lazy('agency_caregiver_list')

    def get_queryset(self):
        return Caregiver.objects.filter(agency=self.request.user.agency)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        AuditLog.objects.create(
            user=self.request.user,
            action='delete',
            model_name='Caregiver',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT')
        )
        return response

class AgencyComplianceView(LoginRequiredMixin, AgencyRequiredMixin, ListView):
    model = Caregiver
    template_name = 'caregivers/agency/compliance.html'
    context_object_name = 'caregivers'

    def get_queryset(self):
        return Caregiver.objects.filter(agency=self.request.user.agency)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agency = self.request.user.agency
        context['agency'] = agency
        context['compliance_summary'] = self.get_compliance_summary()
        context['expiring_certifications'] = self.get_expiring_certifications()
        context['expiring_licenses'] = self.get_expiring_licenses()
        context['hipaa_compliance'] = self.get_hipaa_compliance()
        return context

    def get_compliance_summary(self):
        queryset = self.get_queryset()
        return {
            'total_caregivers': queryset.count(),
            'hipaa_compliant': queryset.filter(hipaa_compliance_status=True).count(),
            'certifications_valid': sum(1 for c in queryset if all(cert.is_valid() for cert in c.certifications.all())),
            'licenses_valid': sum(1 for c in queryset if all(license.is_valid() for license in c.caregiverstatelicense_set.all())),
        }

    def get_expiring_certifications(self):
        return Certification.objects.filter(
            caregiver__agency=self.request.user.agency,
            expiry_date__lte=timezone.now().date() + timedelta(days=30)
        ).select_related('caregiver', 'cert_type')

    def get_expiring_licenses(self):
        return CaregiverStateLicense.objects.filter(
            caregiver__agency=self.request.user.agency,
            expiry_date__lte=timezone.now().date() + timedelta(days=30)
        ).select_related('caregiver', 'state')

    def get_hipaa_compliance(self):
        return {
            'agency_compliance': self.request.user.agency.hipaa_compliance_date is not None,
            'caregiver_compliance': self.get_queryset().filter(hipaa_compliance_status=True).count() / self.get_queryset().count() if self.get_queryset().exists() else 0,
        }

class AgencySettingsView(LoginRequiredMixin, AgencyRequiredMixin, UpdateView):
    model = Agency
    form_class = AgencyForm
    template_name = 'caregivers/agency/settings.html'
    success_url = reverse_lazy('agency_settings')

    def get_object(self):
        return self.request.user.agency

    def form_valid(self, form):
        response = super().form_valid(form)
        AuditLog.objects.create(
            user=self.request.user,
            action='update',
            model_name='Agency',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            changes=form.changed_data
        )
        return response

class AgencyStateLicenseCreateView(LoginRequiredMixin, AgencyRequiredMixin, CreateView):
    model = AgencyStateLicense
    form_class = AgencyStateLicenseForm
    template_name = 'caregivers/agency/state_license_form.html'
    success_url = reverse_lazy('agency_settings')

    def form_valid(self, form):
        form.instance.agency = self.request.user.agency
        response = super().form_valid(form)
        AuditLog.objects.create(
            user=self.request.user,
            action='create',
            model_name='AgencyStateLicense',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT')
        )
        return response

class AgencyStateLicenseUpdateView(LoginRequiredMixin, AgencyRequiredMixin, UpdateView):
    model = AgencyStateLicense
    form_class = AgencyStateLicenseForm
    template_name = 'caregivers/agency/state_license_form.html'
    success_url = reverse_lazy('agency_settings')

    def get_queryset(self):
        return AgencyStateLicense.objects.filter(agency=self.request.user.agency)

    def form_valid(self, form):
        response = super().form_valid(form)
        AuditLog.objects.create(
            user=self.request.user,
            action='update',
            model_name='AgencyStateLicense',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            changes=form.changed_data
        )
        return response

class AgencyStateLicenseDeleteView(LoginRequiredMixin, AgencyRequiredMixin, DeleteView):
    model = AgencyStateLicense
    template_name = 'caregivers/agency/state_license_confirm_delete.html'
    success_url = reverse_lazy('agency_settings')

    def get_queryset(self):
        return AgencyStateLicense.objects.filter(agency=self.request.user.agency)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        AuditLog.objects.create(
            user=self.request.user,
            action='delete',
            model_name='AgencyStateLicense',
            record_id=str(self.object.id),
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT')
        )
        return response

class CaregiverListView(ListView):
    model = Caregiver
    template_name = 'caregivers/caregiver_list.html'
    context_object_name = 'caregivers'

    def get_queryset(self):
        queryset = Caregiver.objects.all()
        form = CaregiverFilterForm(self.request.GET)
        
        if form.is_valid():
            search = form.cleaned_data.get('search')
            status = form.cleaned_data.get('status')
            state = form.cleaned_data.get('state')
            certification = form.cleaned_data.get('certification')
            min_years_experience = form.cleaned_data.get('min_years_experience')

            if search:
                queryset = queryset.filter(
                    Q(name__icontains=search) |
                    Q(specialties__icontains=search)
                )

            if status:
                queryset = queryset.filter(status=status)

            if state:
                queryset = queryset.filter(states_licensed=state)

            if certification:
                queryset = queryset.filter(certifications__cert_type=certification)

            if min_years_experience:
                queryset = queryset.filter(
                    experiences__start_date__lte=timezone.now().date() - timedelta(days=365 * min_years_experience)
                )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CaregiverFilterForm(self.request.GET)
        return context

class CaregiverDetailView(DetailView):
    model = Caregiver
    template_name = 'caregivers/caregiver_detail.html'
    context_object_name = 'caregiver'

class CaregiverCreateView(CreateView):
    model = Caregiver
    form_class = CaregiverForm
    template_name = 'caregivers/caregiver_form.html'
    success_url = reverse_lazy('caregiver_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Caregiver created successfully.')
        return response

class CaregiverUpdateView(UpdateView):
    model = Caregiver
    form_class = CaregiverForm
    template_name = 'caregivers/caregiver_form.html'

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Caregiver updated successfully.')
        return response

class CaregiverDeleteView(DeleteView):
    model = Caregiver
    template_name = 'caregivers/caregiver_confirm_delete.html'
    success_url = reverse_lazy('caregiver_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Caregiver deleted successfully.')
        return response

class CertificationCreateView(CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'caregivers/certification_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caregiver'] = Caregiver.objects.get(pk=self.kwargs['caregiver_id'])
        # Add state renewal cycles for JavaScript
        context['state_renewal_cycles'] = {
            state.id: state.renewal_cycle_months
            for state in State.objects.all()
        }
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['caregiver'] = Caregiver.objects.get(pk=self.kwargs['caregiver_id'])
        return kwargs

    def form_valid(self, form):
        form.instance.caregiver = Caregiver.objects.get(pk=self.kwargs['caregiver_id'])
        response = super().form_valid(form)
        messages.success(self.request, 'Certification added successfully.')
        return response

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.kwargs['caregiver_id']})

class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'caregivers/experience_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caregiver'] = Caregiver.objects.get(pk=self.kwargs['caregiver_id'])
        return context

    def form_valid(self, form):
        form.instance.caregiver_id = self.kwargs['caregiver_id']
        response = super().form_valid(form)
        messages.success(self.request, 'Experience added successfully.')
        return response

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.kwargs['caregiver_id']})

class ExperienceUpdateView(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'caregivers/experience_form.html'

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.caregiver.pk})

class ExperienceDeleteView(DeleteView):
    model = Experience
    template_name = 'caregivers/experience_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.caregiver.pk})

class CaregiverStateLicenseCreateView(LoginRequiredMixin, CreateView):
    model = CaregiverStateLicense
    form_class = CaregiverStateLicenseForm
    template_name = 'caregivers/caregiver_state_license_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['caregiver'] = self.get_caregiver()
        return kwargs

    def get_caregiver(self):
        return get_object_or_404(Caregiver, pk=self.kwargs['caregiver_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caregiver'] = self.get_caregiver()
        context['states'] = State.objects.all().order_by('name')
        return context

    def form_valid(self, form):
        form.instance.caregiver = self.get_caregiver()
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('caregiver_detail', kwargs={'pk': self.kwargs['caregiver_id']})

class CaregiverStateLicenseUpdateView(LoginRequiredMixin, UpdateView):
    model = CaregiverStateLicense
    form_class = CaregiverStateLicenseForm
    template_name = 'caregivers/caregiver_state_license_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['caregiver'] = self.object.caregiver
        return kwargs

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.caregiver.pk})

class CaregiverStateLicenseDeleteView(LoginRequiredMixin, DeleteView):
    model = CaregiverStateLicense
    template_name = 'caregivers/caregiver_state_license_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.caregiver.pk})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('caregiver_list')
    else:
        form = LoginForm()
    return render(request, 'caregivers/auth/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('caregiver_list')
    else:
        form = RegisterForm()
    return render(request, 'caregivers/auth/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Successfully logged out!')
    return redirect('login')

class CertificationUpdateView(UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'caregivers/certification_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['caregiver'] = self.object.caregiver
        return kwargs

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.caregiver.pk})

class CertificationDeleteView(DeleteView):
    model = Certification
    template_name = 'caregivers/certification_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.object.caregiver.pk})

class AgencyListView(ListView):
    model = Agency
    template_name = 'caregivers/agency_list.html'
    context_object_name = 'agencies'

class AgencyDetailView(DetailView):
    model = Agency
    template_name = 'caregivers/agency_detail.html'
    context_object_name = 'agency'

class AgencyCreateView(CreateView):
    model = Agency
    form_class = AgencyForm
    template_name = 'caregivers/agency_form.html'
    success_url = reverse_lazy('agency_list')

class AgencyUpdateView(UpdateView):
    model = Agency
    form_class = AgencyForm
    template_name = 'caregivers/agency_form.html'
    success_url = reverse_lazy('agency_list')

class AgencyDeleteView(DeleteView):
    model = Agency
    template_name = 'caregivers/agency_confirm_delete.html'
    success_url = reverse_lazy('agency_list')

@login_required
def experience_list(request):
    caregiver = request.user.caregiver
    experiences = caregiver.experiences.all()
    return render(request, 'caregivers/experience_list.html', {
        'experiences': experiences
    })

@login_required
def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.caregiver = request.user.caregiver
            experience.save()
            messages.success(request, 'Experience added successfully.')
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    
    return render(request, 'caregivers/experience_form.html', {
        'form': form,
        'title': 'Add Experience'
    })

@login_required
def edit_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk, caregiver=request.user.caregiver)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience updated successfully.')
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=experience)
    
    return render(request, 'caregivers/experience_form.html', {
        'form': form,
        'title': 'Edit Experience'
    })

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES['resume_file']
            
            # Extract text from resume
            if resume_file.name.endswith('.pdf'):
                text = extract_text_from_pdf(resume_file)
            elif resume_file.name.endswith('.docx'):
                text = extract_text_from_docx(resume_file)
            else:
                messages.error(request, 'Unsupported file format. Please upload a PDF or Word document.')
                return redirect('upload_resume')
            
            # Parse resume
            parser = ResumeParserService()
            parsed_data = parser.parse_resume(text)
            
            # Create database objects
            experiences, skills, certifications = parser.create_experience_objects(
                request.user.caregiver,
                parsed_data
            )
            
            messages.success(request, f'Successfully extracted {len(experiences)} experiences, {len(skills)} skills, and {len(certifications)} certifications from your resume.')
            return redirect('experience_list')
    else:
        form = ResumeUploadForm()
    
    return render(request, 'caregivers/upload_resume.html', {
        'form': form
    })

def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    text = ""
    doc = docx.Document(file)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text
    