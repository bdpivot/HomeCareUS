from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
from .models import (
    User, Agency, State, StateWaiverProgram, CertificationType,
    Caregiver, Experience, CaregiverStateLicense, AgencyStateLicense,
    Certification, AuditLog, CaregiverExperience, Skill
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_agency_admin', 'agency')
    list_filter = ('is_agency_admin', 'agency')
    search_fields = ('email', 'username')

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'npi_number', 'tax_id', 'email', 'phone')
    search_fields = ('name', 'npi_number', 'tax_id')
    list_filter = ('hipaa_compliance_date',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'allows_family_caregivers', 'has_agency_option')
    search_fields = ('name', 'abbreviation')
    list_filter = ('allows_family_caregivers', 'has_agency_option', 'has_consumer_directed_option', 'has_self_directed_option')

@admin.register(StateWaiverProgram)
class StateWaiverProgramAdmin(admin.ModelAdmin):
    list_display = ('state', 'program_name', 'administering_agency', 'effective_date')
    list_filter = ('state', 'effective_date')
    search_fields = ('program_name', 'administering_agency')

@admin.register(CertificationType)
class CertificationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_medicaid_certified', 'is_hospice_certified', 'is_private_duty', 'required_training_hours')
    list_filter = ('is_medicaid_certified', 'is_hospice_certified', 'is_private_duty')
    search_fields = ('name',)

@admin.register(Caregiver)
class CaregiverAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'agency', 'is_medicaid_certified', 'is_hospice_certified')
    list_filter = ('status', 'agency', 'is_medicaid_certified', 'is_hospice_certified')
    search_fields = ('name', 'specialties')
    raw_id_fields = ('agency', 'created_by', 'updated_by')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('caregiver', 'position', 'organization', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'start_date')
    search_fields = ('position', 'organization')
    raw_id_fields = ('caregiver',)

@admin.register(CaregiverStateLicense)
class CaregiverStateLicenseAdmin(admin.ModelAdmin):
    list_display = ('caregiver', 'state', 'license_number', 'status', 'verification_status', 'expiry_date')
    list_filter = ('status', 'verification_status', 'state')
    search_fields = ('license_number', 'caregiver__name', 'state__name')
    raw_id_fields = ('caregiver', 'state')

@admin.register(AgencyStateLicense)
class AgencyStateLicenseAdmin(admin.ModelAdmin):
    list_display = ('agency', 'state', 'license_number', 'status', 'verification_status', 'expiry_date')
    list_filter = ('status', 'verification_status', 'state')
    search_fields = ('license_number', 'agency__name', 'state__name')
    raw_id_fields = ('agency', 'state')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'status', 'verification_status', 'issue_date', 'expiry_date']
    list_filter = ['status', 'verification_status', 'certification_type']
    search_fields = ['name', 'number', 'caregiver__name']
    raw_id_fields = ['caregiver', 'certification_type']
    date_hierarchy = 'issue_date'
    readonly_fields = ['created_at', 'updated_at', 'last_verified_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('caregiver', 'certification_type', 'name', 'number', 'issuing_organization')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date', 'is_current')
        }),
        ('Status', {
            'fields': ('status', 'verification_status', 'verification_url')
        }),
        ('Documents', {
            'fields': ('document', 'verification_date', 'verification_notes')
        }),
        ('Additional Information', {
            'fields': ('training_hours_completed', 'background_check_date', 'fingerprinting_date',
                      'medicaid_cert_date', 'surety_bond_amount', 'surety_bond_expiry')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at', 'last_verified_at', 'verification_source'),
            'classes': ('collapse',)
        })
    )

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'action', 'model_name', 'record_id', 'user')
    list_filter = ('action', 'model_name', 'timestamp')
    search_fields = ('record_id', 'model_name', 'user__username')
    readonly_fields = ('timestamp', 'action', 'model_name', 'record_id', 'ip_address', 'user_agent', 'changes', 'user')
    raw_id_fields = ('user',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(CaregiverExperience)
class CaregiverExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'employer_name', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current']
    search_fields = ['position', 'employer_name', 'description', 'caregiver__name']
    raw_id_fields = ['caregiver']
    filter_horizontal = ['skills', 'certifications']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name', 'category', 'description']
    list_filter = ['category']
