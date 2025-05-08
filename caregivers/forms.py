from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from .models import (
    Caregiver, Certification, Experience, State, 
    CertificationType, CaregiverStateLicense, Agency, AgencyStateLicense, User,
    CaregiverExperience, Skill
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = [
            'name', 'npi_number', 'tax_id', 'address', 'phone', 'email', 'website',
            'hipaa_compliance_date', 'hipaa_compliance_officer', 'hipaa_compliance_contact'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'hipaa_compliance_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_npi_number(self):
        npi = self.cleaned_data['npi_number']
        if not npi.isdigit() or len(npi) != 10:
            raise ValidationError('NPI number must be 10 digits')
        return npi

    def clean_tax_id(self):
        tax_id = self.cleaned_data['tax_id']
        # Remove any non-alphanumeric characters
        tax_id = ''.join(c for c in tax_id if c.isalnum())
        if not tax_id:
            raise ValidationError('Tax ID is required')
        return tax_id

class AgencyStateLicenseForm(forms.ModelForm):
    class Meta:
        model = AgencyStateLicense
        fields = ['state', 'license_number', 'issue_date', 'expiry_date', 'status', 'verification_status', 'verification_notes']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'verification_notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.agency = kwargs.pop('agency', None)
        super().__init__(*args, **kwargs)
        if self.agency:
            self.fields['state'].queryset = State.objects.exclude(
                id__in=self.agency.states_licensed.values_list('id', flat=True)
            )

    def clean(self):
        cleaned_data = super().clean()
        issue_date = cleaned_data.get('issue_date')
        expiry_date = cleaned_data.get('expiry_date')
        state = cleaned_data.get('state')

        if issue_date and expiry_date and issue_date >= expiry_date:
            raise ValidationError('Expiry date must be after issue date')

        if state and self.agency:
            # Check if agency already has a license for this state
            existing_license = AgencyStateLicense.objects.filter(
                agency=self.agency,
                state=state,
                status='active'
            ).exclude(pk=self.instance.pk if self.instance else None).first()

            if existing_license:
                raise ValidationError(f'Agency already has an active license for {state.name}')

        return cleaned_data

class CaregiverForm(forms.ModelForm):
    class Meta:
        model = Caregiver
        fields = [
            'name', 'specialties', 'status',
            'is_medicaid_certified', 'is_hospice_certified', 'is_private_duty',
            'hipaa_training_date', 'hipaa_training_expiry', 'hipaa_compliance_status',
            'hipaa_compliance_notes'
        ]
        widgets = {
            'specialties': forms.Textarea(attrs={'rows': 3}),
            'hipaa_compliance_notes': forms.Textarea(attrs={'rows': 3}),
            'hipaa_training_date': forms.DateInput(attrs={'type': 'date'}),
            'hipaa_training_expiry': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hipaa_training_date = cleaned_data.get('hipaa_training_date')
        hipaa_training_expiry = cleaned_data.get('hipaa_training_expiry')
        hipaa_compliance_status = cleaned_data.get('hipaa_compliance_status')

        if hipaa_compliance_status and not hipaa_training_date:
            raise ValidationError('HIPAA training date is required when compliance status is active')

        if hipaa_training_date and hipaa_training_expiry and hipaa_training_date >= hipaa_training_expiry:
            raise ValidationError('HIPAA training expiry date must be after training date')

        return cleaned_data

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuing_organization', 'issue_date', 'expiry_date', 'is_current', 'verification_url']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.caregiver = kwargs.pop('caregiver', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        issue_date = cleaned_data.get('issue_date')
        expiry_date = cleaned_data.get('expiry_date')
        certification_type = cleaned_data.get('certification_type')

        if issue_date and expiry_date and issue_date >= expiry_date:
            raise ValidationError('Expiry date must be after issue date')

        if certification_type and self.caregiver:
            # Check if caregiver already has this certification
            existing_cert = Certification.objects.filter(
                caregiver=self.caregiver,
                certification_type=certification_type,
                expiry_date__gt=timezone.now().date()
            ).exclude(pk=self.instance.pk if self.instance else None).first()

            if existing_cert:
                raise ValidationError(f'Caregiver already has an active {certification_type.name} certification')

        return cleaned_data

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = CaregiverExperience
        fields = ['employer_name', 'position', 'start_date', 'end_date', 'is_current', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        is_current = cleaned_data.get('is_current')

        if not is_current and start_date and end_date and start_date >= end_date:
            raise ValidationError('End date must be after start date')

        if is_current and end_date:
            raise ValidationError('End date should not be set for current positions')

        return cleaned_data

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }

class ResumeUploadForm(forms.Form):
    resume_file = forms.FileField(
        label='Upload Resume',
        help_text='Upload a PDF or Word document containing your resume'
    )
    parse_skills = forms.BooleanField(
        label='Extract Skills',
        required=False,
        initial=True
    )
    parse_certifications = forms.BooleanField(
        label='Extract Certifications',
        required=False,
        initial=True
    )

class CaregiverStateLicenseForm(forms.ModelForm):
    class Meta:
        model = CaregiverStateLicense
        fields = ['state', 'license_number', 'issue_date', 'expiry_date', 'verification_status', 'verification_notes']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'verification_notes': forms.Textarea(attrs={'rows': 3}),
            'state': forms.Select(attrs={
                'class': 'form-select state-select',
                'data-live-search': 'true',
                'data-size': '10',
            }),
        }

    def __init__(self, *args, **kwargs):
        self.caregiver = kwargs.pop('caregiver', None)
        super().__init__(*args, **kwargs)
        
        # Set default expiry date to 1 year from today
        today = timezone.now().date()
        self.fields['issue_date'].initial = today
        self.fields['expiry_date'].initial = today + timedelta(days=365)
        
        # Get all states that the caregiver doesn't already have a license for
        if self.caregiver:
            # Get states the caregiver already has licenses for
            existing_licenses = CaregiverStateLicense.objects.filter(
                caregiver=self.caregiver,
                expiry_date__gt=timezone.now().date()
            ).values_list('state_id', flat=True)
            
            # Get all states except the ones the caregiver already has active licenses for
            available_states = State.objects.exclude(id__in=existing_licenses)
        else:
            available_states = State.objects.all()
        
        # Create choices with additional information
        state_choices = []
        for state in available_states:
            label = f"{state.name} ({state.code}) - {state.region}"
            if state.requires_medicaid_cert:
                label += " [Medicaid Required]"
            if state.requires_background_check:
                label += " [Background Check Required]"
            state_choices.append((state.id, label))
        
        self.fields['state'].choices = [('', 'Select a state...')] + state_choices

    def clean(self):
        cleaned_data = super().clean()
        issue_date = cleaned_data.get('issue_date')
        expiry_date = cleaned_data.get('expiry_date')
        state = cleaned_data.get('state')

        if issue_date and expiry_date:
            if issue_date >= expiry_date:
                raise ValidationError('Expiry date must be after issue date')
            
            # Calculate the duration in days
            duration = (expiry_date - issue_date).days
            
            # Add a warning for licenses shorter than 1 year
            if duration < 365:
                self.add_warning('expiry_date', 
                    f'Warning: This license duration ({duration} days) is less than the standard 1 year. '
                    'Please verify this is correct.')
            
            # Add a warning for licenses longer than 2 years
            elif duration > 730:
                self.add_warning('expiry_date',
                    f'Warning: This license duration ({duration} days) is longer than 2 years. '
                    'Please verify this is correct.')

        if expiry_date and expiry_date <= timezone.now().date():
            raise ValidationError('Expiry date must be in the future')

        if state and self.caregiver:
            # Check if caregiver already has a license for this state
            existing_license = CaregiverStateLicense.objects.filter(
                caregiver=self.caregiver,
                state=state,
                expiry_date__gt=timezone.now().date()
            ).exclude(pk=self.instance.pk if self.instance else None).first()

            if existing_license:
                raise ValidationError(f'Caregiver already has an active license for {state.name}')

        return cleaned_data

    def add_warning(self, field, message):
        """Add a warning message to a field without preventing form submission."""
        if not hasattr(self, '_warnings'):
            self._warnings = {}
        if field not in self._warnings:
            self._warnings[field] = []
        self._warnings[field].append(message)

    @property
    def warnings(self):
        """Return any warnings that were added during validation."""
        return getattr(self, '_warnings', {})

class CaregiverFilterForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search by name or specialty'}))
    status = forms.ChoiceField(required=False, choices=[('', 'All Statuses')] + Caregiver.STATUS_CHOICES)
    state = forms.ModelChoiceField(required=False, queryset=State.objects.all(), empty_label='All States')
    certification = forms.ModelChoiceField(required=False, queryset=CertificationType.objects.all(), empty_label='All Certifications')
    min_years_experience = forms.IntegerField(required=False, min_value=0, max_value=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'
            field.widget.attrs['style'] = 'min-height: 38px;'

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number'
        })
    )
    is_agency_admin = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    is_caregiver = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'phone', 'is_agency_admin', 'is_caregiver']