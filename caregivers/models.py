from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, unique=True)
    training_hours_required = models.IntegerField(default=0)
    renewal_cycle_months = models.IntegerField(default=12)
    requires_background_check = models.BooleanField(default=True)
    requires_fingerprinting = models.BooleanField(default=False)
    requires_medicaid_cert = models.BooleanField(default=False)
    requires_surety_bond = models.BooleanField(default=False)
    min_bond_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    background_check_validity_months = models.IntegerField(default=12)
    fingerprinting_validity_months = models.IntegerField(default=12)
    medicaid_cert_validity_months = models.IntegerField(default=12)
    surety_bond_validity_months = models.IntegerField(default=12)
    requires_continuing_education = models.BooleanField(default=False)
    continuing_education_hours_required = models.IntegerField(default=0)
    continuing_education_cycle_months = models.IntegerField(default=12)
    requires_cpr_certification = models.BooleanField(default=True)
    cpr_cert_validity_months = models.IntegerField(default=12)
    requires_first_aid_certification = models.BooleanField(default=True)
    first_aid_cert_validity_months = models.IntegerField(default=12)
    requires_tb_test = models.BooleanField(default=True)
    tb_test_validity_months = models.IntegerField(default=12)
    requires_flu_shot = models.BooleanField(default=True)
    requires_covid_vaccination = models.BooleanField(default=True)
    requires_drug_test = models.BooleanField(default=True)
    drug_test_validity_months = models.IntegerField(default=12)
    requires_physical_exam = models.BooleanField(default=True)
    physical_exam_validity_months = models.IntegerField(default=12)
    requires_auto_insurance = models.BooleanField(default=True)
    min_auto_insurance_coverage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requires_liability_insurance = models.BooleanField(default=True)
    min_liability_insurance_coverage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requires_workers_comp_insurance = models.BooleanField(default=True)
    requires_health_insurance = models.BooleanField(default=True)
    requires_disability_insurance = models.BooleanField(default=True)
    requires_life_insurance = models.BooleanField(default=True)
    min_life_insurance_coverage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requires_emergency_contact = models.BooleanField(default=True)
    requires_emergency_backup = models.BooleanField(default=True)
    requires_availability_schedule = models.BooleanField(default=True)
    requires_service_area_definition = models.BooleanField(default=True)
    requires_vehicle_registration = models.BooleanField(default=True)
    requires_drivers_license = models.BooleanField(default=True)
    requires_vehicle_inspection = models.BooleanField(default=True)
    vehicle_inspection_validity_months = models.IntegerField(default=12)
    requires_vehicle_maintenance_log = models.BooleanField(default=True)
    requires_incident_reporting = models.BooleanField(default=True)
    requires_medication_administration_training = models.BooleanField(default=True)
    requires_infection_control_training = models.BooleanField(default=True)
    requires_emergency_procedures_training = models.BooleanField(default=True)
    requires_cultural_competency_training = models.BooleanField(default=True)
    requires_abuse_prevention_training = models.BooleanField(default=True)
    requires_confidentiality_training = models.BooleanField(default=True)
    requires_hipaa_training = models.BooleanField(default=True)
    hipaa_training_validity_months = models.IntegerField(default=12)
    requires_osha_training = models.BooleanField(default=True)
    osha_training_validity_months = models.IntegerField(default=12)
    requires_bloodborne_pathogens_training = models.BooleanField(default=True)
    bloodborne_pathogens_training_validity_months = models.IntegerField(default=12)
    requires_fire_safety_training = models.BooleanField(default=True)
    fire_safety_training_validity_months = models.IntegerField(default=12)
    requires_emergency_evacuation_training = models.BooleanField(default=True)
    emergency_evacuation_training_validity_months = models.IntegerField(default=12)
    requires_disaster_preparedness_training = models.BooleanField(default=True)
    disaster_preparedness_training_validity_months = models.IntegerField(default=12)
    requires_emergency_communication_training = models.BooleanField(default=True)
    emergency_communication_training_validity_months = models.IntegerField(default=12)
    requires_emergency_equipment_training = models.BooleanField(default=True)
    emergency_equipment_training_validity_months = models.IntegerField(default=12)
    requires_emergency_medication_training = models.BooleanField(default=True)
    emergency_medication_training_validity_months = models.IntegerField(default=12)
    requires_emergency_transportation_training = models.BooleanField(default=True)
    emergency_transportation_training_validity_months = models.IntegerField(default=12)
    requires_emergency_documentation_training = models.BooleanField(default=True)
    emergency_documentation_training_validity_months = models.IntegerField(default=12)
    requires_emergency_follow_up_training = models.BooleanField(default=True)
    emergency_follow_up_training_validity_months = models.IntegerField(default=12)
    requires_emergency_debriefing_training = models.BooleanField(default=True)
    emergency_debriefing_training_validity_months = models.IntegerField(default=12)
    requires_emergency_quality_improvement_training = models.BooleanField(default=True)
    emergency_quality_improvement_training_validity_months = models.IntegerField(default=12)
    requires_emergency_risk_management_training = models.BooleanField(default=True)
    emergency_risk_management_training_validity_months = models.IntegerField(default=12)
    requires_emergency_legal_compliance_training = models.BooleanField(default=True)
    emergency_legal_compliance_training_validity_months = models.IntegerField(default=12)
    requires_emergency_ethics_training = models.BooleanField(default=True)
    emergency_ethics_training_validity_months = models.IntegerField(default=12)
    requires_emergency_cultural_competency_training = models.BooleanField(default=True)
    emergency_cultural_competency_training_validity_months = models.IntegerField(default=12)
    notes = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['name']),
        ]

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

class Certification(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked'),
        ('suspended', 'Suspended'),
    ]

    VERIFICATION_STATUS_CHOICES = [
        ('pending', 'Pending Verification'),
        ('verified', 'Verified'),
        ('failed', 'Verification Failed'),
        ('expired', 'Verification Expired'),
    ]

    caregiver = models.ForeignKey('Caregiver', related_name='certifications', on_delete=models.CASCADE)
    cert_type = models.ForeignKey(CertificationType, on_delete=models.PROTECT, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True)
    number = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    document = models.FileField(upload_to='certifications/', null=True, blank=True)
    
    # Verification fields
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS_CHOICES, default='pending')
    verification_date = models.DateTimeField(null=True, blank=True)
    verification_notes = models.TextField(blank=True)
    
    # Training and compliance
    training_hours_completed = models.IntegerField(default=0)
    background_check_date = models.DateField(null=True, blank=True)
    fingerprinting_date = models.DateField(null=True, blank=True)
    medicaid_cert_date = models.DateField(null=True, blank=True)
    surety_bond_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    surety_bond_expiry = models.DateField(null=True, blank=True)
    
    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_verified_at = models.DateTimeField(null=True, blank=True)
    verification_source = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['-issue_date']
        indexes = [
            models.Index(fields=['status', 'verification_status']),
            models.Index(fields=['expiry_date']),
        ]

    def __str__(self):
        return f"{self.cert_type.name if self.cert_type else 'Unknown'} ({self.number}) - {self.state.code if self.state else 'No State'}"

    @property
    def is_expired(self):
        return self.expiry_date < timezone.now().date()

    @property
    def days_until_expiry(self):
        return (self.expiry_date - timezone.now().date()).days

    @property
    def requires_renewal(self):
        return self.days_until_expiry <= 90  # Alert 90 days before expiry

    def verify(self, source, notes=''):
        self.verification_status = 'verified'
        self.verification_date = timezone.now()
        self.last_verified_at = timezone.now()
        self.verification_source = source
        self.verification_notes = notes
        self.save()

class Caregiver(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave'),
        ('terminated', 'Terminated'),
    ]

    name = models.CharField(max_length=100)
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE)
    specialties = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    states_licensed = models.ManyToManyField(State, through='CaregiverStateLicense', blank=True)
    is_medicaid_certified = models.BooleanField(default=False)
    is_hospice_certified = models.BooleanField(default=False)
    is_private_duty = models.BooleanField(default=False)
    
    # HIPAA Compliance Fields
    hipaa_training_date = models.DateField(null=True, blank=True)
    hipaa_training_expiry = models.DateField(null=True, blank=True)
    hipaa_compliance_status = models.BooleanField(default=False)
    hipaa_compliance_notes = models.TextField(blank=True)
    
    # Security Fields
    two_factor_enabled = models.BooleanField(default=False)
    last_password_change = models.DateTimeField(null=True, blank=True)
    failed_login_attempts = models.IntegerField(default=0)
    account_locked_until = models.DateTimeField(null=True, blank=True)
    
    # Audit Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_caregivers')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_caregivers')

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['agency']),
            models.Index(fields=['hipaa_compliance_status']),
        ]

class CaregiverStateLicense(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)
    verification_status = models.CharField(max_length=20, choices=Certification.VERIFICATION_STATUS_CHOICES, default='pending')
    verification_date = models.DateTimeField(null=True, blank=True)
    verification_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['caregiver', 'state']

    def __str__(self):
        return f"{self.caregiver.name} - {self.state.code} License"

class Experience(models.Model):
    caregiver = models.ForeignKey(Caregiver, related_name='experiences', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} at {self.organization}"

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('view', 'View'),
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('export', 'Export'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    record_id = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True)
    user_agent = models.TextField(null=True)
    changes = models.JSONField(null=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['user', 'action']),
            models.Index(fields=['model_name', 'record_id']),
        ]

class Agency(models.Model):
    name = models.CharField(max_length=200)
    npi_number = models.CharField(max_length=10, unique=True)  # National Provider Identifier
    tax_id = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    states_licensed = models.ManyToManyField('State', through='AgencyStateLicense')
    hipaa_compliance_date = models.DateField(null=True)
    hipaa_compliance_officer = models.CharField(max_length=100, null=True)
    hipaa_compliance_contact = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AgencyStateLicense(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)
    verification_status = models.CharField(max_length=20, choices=Certification.VERIFICATION_STATUS_CHOICES, default='pending')
    verification_date = models.DateTimeField(null=True, blank=True)
    verification_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['agency', 'state']

    def __str__(self):
        return f"{self.agency.name} - {self.state.code} License"