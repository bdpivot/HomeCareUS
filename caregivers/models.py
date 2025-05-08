from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=20, blank=True)
    is_agency_admin = models.BooleanField(default=False)
    agency = models.ForeignKey('Agency', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

class Agency(models.Model):
    name = models.CharField(default='Unnamed Agency', max_length=200)
    npi_number = models.CharField(default='0000000000', max_length=10, unique=True)
    tax_id = models.CharField(default='00-0000000', max_length=20, unique=True)
    address = models.TextField(default='Address not provided')
    phone = models.CharField(default='Phone not provided', max_length=20)
    email = models.EmailField(default='email@notprovided.com', max_length=254)
    website = models.URLField(blank=True, null=True)
    hipaa_compliance_date = models.DateField(null=True)
    hipaa_compliance_officer = models.CharField(max_length=100, null=True)
    hipaa_compliance_contact = models.EmailField(max_length=254, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=2, unique=True)
    allows_family_caregivers = models.BooleanField(default=False)
    family_caregiver_requirements = models.TextField(blank=True)
    has_consumer_directed_option = models.BooleanField(default=False)
    has_self_directed_option = models.BooleanField(default=False)
    has_agency_option = models.BooleanField(default=True)
    salary_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    free_training_available = models.BooleanField(default=False)
    free_training_programs = models.TextField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    special_considerations = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['abbreviation']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

class StateWaiverProgram(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='waiver_programs')
    program_name = models.CharField(max_length=200)
    administering_agency = models.CharField(max_length=200)
    services_offered = models.TextField()
    unique_requirements = models.TextField(blank=True)
    annual_training_requirements = models.TextField(blank=True)
    effective_date = models.DateField(null=True, blank=True)
    registry_name = models.CharField(max_length=200, blank=True)
    registry_update_frequency = models.CharField(max_length=50, blank=True)
    required_forms = models.TextField(blank=True)
    future_requirements = models.TextField(blank=True)
    future_requirements_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    allows_family_caregivers = models.BooleanField(default=False)
    family_caregiver_requirements = models.TextField(blank=True)
    has_consumer_directed_option = models.BooleanField(default=False)
    has_self_directed_option = models.BooleanField(default=False)
    has_agency_option = models.BooleanField(default=True)
    salary_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    free_training_available = models.BooleanField(default=False)
    free_training_programs = models.TextField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    special_considerations = models.TextField(blank=True)

    class Meta:
        ordering = ['state', 'program_name']
        indexes = [
            models.Index(fields=['state']),
            models.Index(fields=['program_name']),
            models.Index(fields=['effective_date']),
            models.Index(fields=['future_requirements_date']),
        ]

    def __str__(self):
        return f"{self.state.name} - {self.program_name}"

class CertificationType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_medicaid_certified = models.BooleanField(default=False)
    is_hospice_certified = models.BooleanField(default=False)
    is_private_duty = models.BooleanField(default=False)
    required_training_hours = models.IntegerField(default=0)
    renewal_cycle_months = models.IntegerField(default=12)

    def __str__(self):
        return self.name

class Caregiver(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave'),
        ('terminated', 'Terminated')
    ]

    name = models.CharField(max_length=100)
    specialties = models.CharField(max_length=200)
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='pending',
        max_length=20
    )
    is_medicaid_certified = models.BooleanField(default=False)
    is_hospice_certified = models.BooleanField(default=False)
    is_private_duty = models.BooleanField(default=False)
    hipaa_training_date = models.DateField(blank=True, null=True)
    hipaa_training_expiry = models.DateField(blank=True, null=True)
    hipaa_compliance_status = models.BooleanField(default=False)
    hipaa_compliance_notes = models.TextField(blank=True)
    two_factor_enabled = models.BooleanField(default=False)
    last_password_change = models.DateTimeField(blank=True, null=True)
    failed_login_attempts = models.IntegerField(default=0)
    account_locked_until = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='created_caregivers')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='updated_caregivers')

    def __str__(self):
        return self.name

class Experience(models.Model):
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name='old_experiences')

    def __str__(self):
        return f"{self.position} at {self.organization}"

class CaregiverStateLicense(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name='state_licenses')
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(
        choices=[
            ('active', 'Active'),
            ('pending', 'Pending'),
            ('expired', 'Expired'),
            ('revoked', 'Revoked'),
            ('suspended', 'Suspended')
        ],
        default='pending',
        max_length=20
    )
    document = models.FileField(upload_to='licenses/', blank=True, null=True)
    verification_status = models.CharField(
        choices=[
            ('pending', 'Pending Verification'),
            ('verified', 'Verified'),
            ('failed', 'Verification Failed'),
            ('expired', 'Verification Expired')
        ],
        default='pending',
        max_length=20
    )
    verification_date = models.DateTimeField(blank=True, null=True)
    verification_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['caregiver', 'state', 'license_number']

    def __str__(self):
        return f"{self.caregiver.name} - {self.state.abbreviation} License"

class AgencyStateLicense(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='state_licenses')
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(
        choices=[
            ('active', 'Active'),
            ('pending', 'Pending'),
            ('expired', 'Expired'),
            ('revoked', 'Revoked'),
            ('suspended', 'Suspended')
        ],
        default='pending',
        max_length=20
    )
    document = models.FileField(upload_to='agency_licenses/', blank=True, null=True)
    verification_status = models.CharField(
        choices=[
            ('pending', 'Pending Verification'),
            ('verified', 'Verified'),
            ('failed', 'Verification Failed'),
            ('expired', 'Verification Expired')
        ],
        default='pending',
        max_length=20
    )
    verification_date = models.DateTimeField(blank=True, null=True)
    verification_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['agency', 'state', 'license_number']

    def __str__(self):
        return f"{self.agency.name} - {self.state.abbreviation} License"

class Certification(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked'),
        ('suspended', 'Suspended')
    ]
    
    VERIFICATION_STATUS_CHOICES = [
        ('pending', 'Pending Verification'),
        ('verified', 'Verified'),
        ('failed', 'Verification Failed'),
        ('expired', 'Verification Expired')
    ]

    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name='certifications')
    certification_type = models.ForeignKey(CertificationType, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, default='Unnamed Certification')
    number = models.CharField(max_length=50, default='N/A')
    issuing_organization = models.CharField(max_length=200, default='Unknown Organization')
    issue_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS_CHOICES, default='pending')
    verification_url = models.URLField(blank=True)
    document = models.FileField(upload_to='certifications/', blank=True, null=True)
    verification_date = models.DateTimeField(blank=True, null=True)
    verification_notes = models.TextField(blank=True)
    training_hours_completed = models.IntegerField(default=0)
    background_check_date = models.DateField(blank=True, null=True)
    fingerprinting_date = models.DateField(blank=True, null=True)
    medicaid_cert_date = models.DateField(blank=True, null=True)
    surety_bond_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    surety_bond_expiry = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_verified_at = models.DateTimeField(blank=True, null=True)
    verification_source = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.caregiver.name} - {self.name}"

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(
        choices=[
            ('view', 'View'),
            ('create', 'Create'),
            ('update', 'Update'),
            ('delete', 'Delete'),
            ('export', 'Export')
        ],
        max_length=10
    )
    model_name = models.CharField(max_length=100)
    record_id = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True)
    user_agent = models.TextField(null=True)
    changes = models.JSONField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['user', 'action']),
            models.Index(fields=['model_name', 'record_id']),
        ]

    def __str__(self):
        return f"{self.action} on {self.model_name} {self.record_id}"

class CaregiverExperience(models.Model):
    caregiver = models.ForeignKey('Caregiver', on_delete=models.CASCADE, related_name='experiences')
    employer_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    skills = models.ManyToManyField('Skill', blank=True)
    certifications = models.ManyToManyField('Certification', blank=True, related_name='experiences')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Caregiver Experience"
        verbose_name_plural = "Caregiver Experiences"

    def __str__(self):
        return f"{self.position} at {self.employer_name}"

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 