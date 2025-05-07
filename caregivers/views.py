from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from .models import Caregiver, Certification, Experience, CaregiverStateLicense, Agency, AgencyStateLicense, AuditLog
from .forms import CaregiverForm, CertificationForm, ExperienceForm, CaregiverStateLicenseForm, AgencyForm, AgencyStateLicenseForm

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
            # Filter by status
            if form.cleaned_data['status']:
                queryset = queryset.filter(status=form.cleaned_data['status'])
            
            # Filter by agency
            if form.cleaned_data['agency']:
                queryset = queryset.filter(agency=form.cleaned_data['agency'])
            
            # Filter by state
            if form.cleaned_data['state']:
                queryset = queryset.filter(states_licensed__id=form.cleaned_data['state'])
            
            # Filter by certification
            if form.cleaned_data['certification']:
                queryset = queryset.filter(certifications__cert_type_id=form.cleaned_data['certification'])
            
            # Filter by name
            if form.cleaned_data['first_name']:
                queryset = queryset.filter(name__icontains=form.cleaned_data['first_name'])
            if form.cleaned_data['last_name']:
                queryset = queryset.filter(name__icontains=form.cleaned_data['last_name'])
            
            # Filter by experience
            if form.cleaned_data['experience_years']:
                min_date = timezone.now().date() - timedelta(days=365 * form.cleaned_data['experience_years'])
                queryset = queryset.filter(
                    Q(experiences__start_date__lte=min_date) &
                    (Q(experiences__end_date__gte=min_date) | Q(experiences__is_current=True))
                ).distinct()
        
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = CaregiverFilterForm(self.request.GET)
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

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Caregiver, Certification, Experience
from .forms import CaregiverForm, CertificationForm, ExperienceForm

# Existing Caregiver views...

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
        kwargs['caregiver_id'] = self.kwargs['caregiver_id']
        return kwargs

    def form_valid(self, form):
        form.instance.caregiver_id = self.kwargs['caregiver_id']
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

class CaregiverStateLicenseCreateView(CreateView):
    model = CaregiverStateLicense
    form_class = CaregiverStateLicenseForm
    template_name = 'caregivers/caregiver_state_license_form.html'

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
        kwargs['caregiver_id'] = self.kwargs['caregiver_id']
        return kwargs

    def form_valid(self, form):
        form.instance.caregiver_id = self.kwargs['caregiver_id']
        response = super().form_valid(form)
        messages.success(self.request, 'State license added successfully.')
        return response

    def get_success_url(self):
        return reverse_lazy('caregiver_detail', kwargs={'pk': self.kwargs['caregiver_id']})
    