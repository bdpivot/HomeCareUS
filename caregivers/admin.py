from django.contrib import admin

# Register your models here.
from .models import Caregiver, Certification, Experience, State, CertificationType, CaregiverStateLicense

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'training_hours_required', 'renewal_cycle_months', 
                   'requires_background_check', 'requires_fingerprinting', 'requires_medicaid_cert')
    list_filter = ('requires_background_check', 'requires_fingerprinting', 'requires_medicaid_cert')
    search_fields = ('name', 'code')

@admin.register(CertificationType)
class CertificationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_training_hours', 'renewal_cycle_months',
                   'is_medicaid_certified', 'is_hospice_certified', 'is_private_duty')
    list_filter = ('is_medicaid_certified', 'is_hospice_certified', 'is_private_duty')
    search_fields = ('name', 'description')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('cert_type', 'state', 'number', 'caregiver', 'issue_date', 
                   'expiry_date', 'status', 'verification_status')
    list_filter = ('status', 'verification_status', 'state', 'cert_type')
    search_fields = ('number', 'caregiver__name', 'cert_type__name')
    date_hierarchy = 'issue_date'
    readonly_fields = ('created_at', 'updated_at', 'last_verified_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('caregiver', 'cert_type', 'state', 'number', 'status')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Verification', {
            'fields': ('verification_status', 'verification_date', 'verification_notes',
                      'verification_source', 'last_verified_at')
        }),
        ('Compliance', {
            'fields': ('training_hours_completed', 'background_check_date',
                      'fingerprinting_date', 'medicaid_cert_date')
        }),
        ('Surety Bond', {
            'fields': ('surety_bond_amount', 'surety_bond_expiry')
        }),
        ('Document', {
            'fields': ('document',)
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CaregiverStateLicense)
class CaregiverStateLicenseAdmin(admin.ModelAdmin):
    list_display = ('caregiver', 'state', 'license_number', 'issue_date', 
                   'expiry_date', 'is_active', 'verification_status')
    list_filter = ('is_active', 'verification_status', 'state')
    search_fields = ('caregiver__name', 'license_number', 'state__name')
    date_hierarchy = 'issue_date'

@admin.register(Caregiver)
class CaregiverAdmin(admin.ModelAdmin):
    list_display = ('name', 'agency', 'status', 'is_medicaid_certified', 
                   'is_hospice_certified', 'is_private_duty')
    list_filter = ('status', 'is_medicaid_certified', 'is_hospice_certified', 
                  'is_private_duty')
    search_fields = ('name', 'agency', 'specialties')
    readonly_fields = ('states_licensed',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('caregiver', 'position', 'organization', 'start_date', 
                   'end_date', 'is_current')
    list_filter = ('is_current', 'organization')
    search_fields = ('caregiver__name', 'position', 'organization')
    date_hierarchy = 'start_date'
