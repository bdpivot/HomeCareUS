from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from .models import Caregiver, Certification, Experience, State, CertificationType, CaregiverStateLicense, Agency, AgencyStateLicense

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
        fields = ['state', 'license_number', 'issue_date', 'expiry_date', 'is_active', 'verification_status', 'verification_notes']
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
                is_active=True
            ).exclude(pk=self.instance.pk if self.instance else None).first()

            if existing_license:
                raise ValidationError(f'Agency already has an active license for {state.name}')

        return cleaned_data

class CaregiverForm(forms.ModelForm):
    class Meta:
        model = Caregiver
        fields = [
            'name', 'specialties', 'status', 'states_licensed',
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
        fields = ['cert_type', 'issue_date', 'expiry_date', 'verification_status', 'verification_notes']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'verification_notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.caregiver = kwargs.pop('caregiver', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        issue_date = cleaned_data.get('issue_date')
        expiry_date = cleaned_data.get('expiry_date')
        cert_type = cleaned_data.get('cert_type')

        if issue_date and expiry_date and issue_date >= expiry_date:
            raise ValidationError('Expiry date must be after issue date')

        if cert_type and self.caregiver:
            # Check if caregiver already has this certification
            existing_cert = Certification.objects.filter(
                caregiver=self.caregiver,
                cert_type=cert_type,
                expiry_date__gt=timezone.now().date()
            ).exclude(pk=self.instance.pk if self.instance else None).first()

            if existing_cert:
                raise ValidationError(f'Caregiver already has an active {cert_type.name} certification')

        return cleaned_data

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['position', 'organization', 'start_date', 'end_date', 'is_current']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
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

class CaregiverStateLicenseForm(forms.ModelForm):
    class Meta:
        model = CaregiverStateLicense
        fields = ['state', 'license_number', 'issue_date', 'expiry_date', 'verification_status', 'verification_notes']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'verification_notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.caregiver = kwargs.pop('caregiver', None)
        super().__init__(*args, **kwargs)
        if self.caregiver:
            self.fields['state'].queryset = State.objects.exclude(
                id__in=self.caregiver.states_licensed.values_list('id', flat=True)
            )

    def clean(self):
        cleaned_data = super().clean()
        issue_date = cleaned_data.get('issue_date')
        expiry_date = cleaned_data.get('expiry_date')
        state = cleaned_data.get('state')

        if issue_date and expiry_date and issue_date >= expiry_date:
            raise ValidationError('Expiry date must be after issue date')

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