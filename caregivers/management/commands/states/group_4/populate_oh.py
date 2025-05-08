from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates the database with Ohio home health aide requirements'

    def handle(self, *args, **kwargs):
        state_data = {
            'name': '',  # State name
            'code': '',  # Two-letter code
            'abbreviation': '',  # Two-letter abbreviation
            'region': '',  # NORTHEAST, MIDWEST, SOUTH, WEST
            'timezone': '',  # America/New_York, etc.
            'medicaid_program_name': '',
            'medicaid_website': '',
            'licensing_board_name': '',
            'licensing_website': '',
            'licensing_phone': '',
            'licensing_email': '',
            'training_hours_required': 0,
            'renewal_cycle_months': 12,
            'requires_background_check': True,
            'requires_fingerprinting': False,
            'requires_medicaid_cert': False,
            'requires_surety_bond': False,
            'min_bond_amount': None,
            'background_check_validity_months': 12,
            'fingerprinting_validity_months': 12,
            'medicaid_cert_validity_months': 12,
            'surety_bond_validity_months': 12,
            'requires_continuing_education': False,
            'continuing_education_hours_required': 0,
            'continuing_education_cycle_months': 12,
            'requires_cpr_certification': True,
            'cpr_cert_validity_months': 12,
            'requires_first_aid_certification': True,
            'first_aid_cert_validity_months': 12,
            'requires_tb_test': True,
            'tb_test_validity_months': 12,
            'requires_flu_shot': True,
            'requires_covid_vaccination': True,
            'requires_drug_test': True,
            'drug_test_validity_months': 12,
            'requires_physical_exam': True,
            'physical_exam_validity_months': 12,
            'requires_auto_insurance': True,
            'min_auto_insurance_coverage': None,
            'requires_liability_insurance': True,
            'min_liability_insurance_coverage': None,
            'requires_workers_comp_insurance': True,
            'requires_health_insurance': True,
            'requires_disability_insurance': True,
            'requires_life_insurance': True,
            'min_life_insurance_coverage': None,
            'requires_emergency_contact': True,
            'requires_emergency_backup': True,
            'requires_availability_schedule': True,
            'requires_service_area_definition': True,
            'requires_vehicle_registration': True,
            'requires_drivers_license': True,
            'requires_vehicle_inspection': True,
            'vehicle_inspection_validity_months': 12,
            'requires_vehicle_maintenance_log': True,
            'requires_incident_reporting': True,
            'requires_medication_administration_training': True,
            'requires_infection_control_training': True,
            'requires_emergency_procedures_training': True,
            'requires_cultural_competency_training': True,
            'requires_abuse_prevention_training': True,
            'requires_confidentiality_training': True,
            'requires_hipaa_training': True,
            'hipaa_training_validity_months': 12,
            'requires_osha_training': True,
            'osha_training_validity_months': 12,
            'requires_bloodborne_pathogens_training': True,
            'bloodborne_pathogens_training_validity_months': 12,
            'requires_fire_safety_training': True,
            'fire_safety_training_validity_months': 12,
            'requires_emergency_evacuation_training': True,
            'emergency_evacuation_training_validity_months': 12,
            'requires_disaster_preparedness_training': True,
            'disaster_preparedness_training_validity_months': 12,
            'allows_family_caregivers': False,
            'family_caregiver_requirements': '',
            'salary_range_min': None,
            'salary_range_max': None,
            'free_training_available': False,
            'free_training_programs': '',
            'registry_name': '',
            'registry_website': '',
            'registry_phone': '',
            'registry_email': '',
            'future_requirements': '',
            'future_requirements_date': None,
            'unique_features': '',
            'special_considerations': '',
            'has_consumer_directed_option': False,
            'has_self_directed_option': False,
            'has_agency_option': True,
            'requires_evv': False,
            'evv_implementation_date': None,
            'notes': ''
        }

        waiver_programs = [
            {
                'program_name': '',
                'administering_agency': '',
                'services_offered': [],
                'unique_requirements': [],
                'allows_family_caregivers': False,
                'family_caregiver_requirements': [],
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': None,
                'salary_range_max': None,
                'free_training_available': False,
                'free_training_programs': '',
                'website': '',
                'phone': '',
                'email': '',
                'notes': '',
                'future_requirements': [],
                'future_requirements_date': None,
                'special_considerations': []
            }
        ]

        # Create or update state
        state, created = State.objects.get_or_create(
            code=state_data['code'],
            defaults=state_data
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created state {state.name}'))
        else:
            self.stdout.write(self.style.WARNING(f'State {state.name} already exists'))

        # Create or update waiver programs
        for waiver_data in waiver_programs:
            waiver, created = StateWaiverProgram.objects.get_or_create(
                state=state,
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created waiver program {waiver.program_name} for {state.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Waiver program {waiver.program_name} for {state.name} already exists')) 