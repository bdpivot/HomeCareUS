from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Wyoming waiver programs'

    def handle(self, *args, **kwargs):
        wyoming = State.objects.get(abbreviation='WY')
        
        waiver_programs = [
            {
                'state': wyoming,
                'program_name': 'Wyoming Medicaid Home Health Services',
                'administering_agency': 'Wyoming Department of Health, Healthcare Licensing and Surveys',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must be Certified Nursing Assistant (CNA) before HHA certification; must complete 75 hours CNA training (includes 16 hours of home health and clinical training); must complete additional 16 hours of home health aide–specific training (total: 91 hours); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 18 years old; must have high school diploma or GED; must have negative tuberculosis (TB) test; must pass criminal background check; must pass drug test; must have CPR certification',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wyoming Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be Certified Nursing Assistant (CNA) before HHA certification; must complete 75 hours CNA training (includes 16 hours of home health and clinical training); must complete additional 16 hours of home health aide–specific training (total: 91 hours); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 18 years old; must have high school diploma or GED; must have negative tuberculosis (TB) test; must pass criminal background check; must pass drug test; must have CPR certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.wyo.gov/aging/hls/facility-types/home-health-agency-wyoming-licensure-information/',
                'phone': '(307) 777-7123',
                'email': 'hls@wyo.gov'
            },
            {
                'state': wyoming,
                'program_name': 'Home and Community-Based Services (HCBS) Waiver',
                'administering_agency': 'Wyoming Department of Health, Healthcare Licensing and Surveys',
                'services_offered': 'Personal care, respite, homemaker, and assisted living services',
                'unique_requirements': 'Must be Certified Nursing Assistant (CNA) before HHA certification; must complete 75 hours CNA training (includes 16 hours of home health and clinical training); must complete additional 16 hours of home health aide–specific training (total: 91 hours); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 18 years old; must have high school diploma or GED; must have negative tuberculosis (TB) test; must pass criminal background check; must pass drug test; must have CPR certification',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wyoming Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be Certified Nursing Assistant (CNA) before HHA certification; must complete 75 hours CNA training (includes 16 hours of home health and clinical training); must complete additional 16 hours of home health aide–specific training (total: 91 hours); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 18 years old; must have high school diploma or GED; must have negative tuberculosis (TB) test; must pass criminal background check; must pass drug test; must have CPR certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.wyo.gov/waiver-programs-part-of-wyoming-medicaid-renewals/',
                'phone': '(307) 777-7123',
                'email': 'hls@wyo.gov'
            },
            {
                'state': wyoming,
                'program_name': 'Assisted Living Waiver',
                'administering_agency': 'Wyoming Department of Health, Healthcare Licensing and Surveys',
                'services_offered': 'Personal care, respite, homemaker, and assisted living services',
                'unique_requirements': 'Must be Certified Nursing Assistant (CNA) before HHA certification; must complete 75 hours CNA training (includes 16 hours of home health and clinical training); must complete additional 16 hours of home health aide–specific training (total: 91 hours); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 18 years old; must have high school diploma or GED; must have negative tuberculosis (TB) test; must pass criminal background check; must pass drug test; must have CPR certification',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wyoming Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Assisted Living Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be Certified Nursing Assistant (CNA) before HHA certification; must complete 75 hours CNA training (includes 16 hours of home health and clinical training); must complete additional 16 hours of home health aide–specific training (total: 91 hours); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 18 years old; must have high school diploma or GED; must have negative tuberculosis (TB) test; must pass criminal background check; must pass drug test; must have CPR certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.wyo.gov/waiver-programs-part-of-wyoming-medicaid-renewals/',
                'phone': '(307) 777-7123',
                'email': 'hls@wyo.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Wyoming waiver programs')) 