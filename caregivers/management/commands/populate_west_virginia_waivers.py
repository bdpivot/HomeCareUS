from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates West Virginia waiver programs'

    def handle(self, *args, **kwargs):
        west_virginia = State.objects.get(abbreviation='WV')
        
        waiver_programs = [
            {
                'state': west_virginia,
                'program_name': 'West Virginia Medicaid Home Health Services',
                'administering_agency': 'West Virginia Department of Health and Human Resources (DHHR), Office of Health Facility Licensure and Certification',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (federal minimum for HHA certification; required in WV); must complete 16 clinical hours (hands-on, supervised); must pass state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must be at least 18 years old; must have CPR certification; must pass criminal background check; must pass abuse registry check',
                'annual_training_requirements': 'Abuse/neglect/exploitation and dementia training required for registration renewal; OSHA and HIPAA training required for registration renewal; First aid training required for registration renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'West Virginia In-Home Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of training; must complete 16 clinical hours; must pass state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must be at least 18 years old; must have CPR certification; must pass criminal background check; must pass abuse registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://inhomecare.wv.gov/providers/Pages/Requirements.aspx',
                'phone': '(304) 558-0050',
                'email': 'ohflac@wv.gov'
            },
            {
                'state': west_virginia,
                'program_name': 'Aged and Disabled Waiver',
                'administering_agency': 'West Virginia Department of Health and Human Resources (DHHR), Office of Health Facility Licensure and Certification',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (federal minimum for HHA certification; required in WV); must complete 16 clinical hours (hands-on, supervised); must pass state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must be at least 18 years old; must have CPR certification; must pass criminal background check; must pass abuse registry check',
                'annual_training_requirements': 'Abuse/neglect/exploitation and dementia training required for registration renewal; OSHA and HIPAA training required for registration renewal; First aid training required for registration renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'West Virginia In-Home Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Aged and Disabled Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of training; must complete 16 clinical hours; must pass state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must be at least 18 years old; must have CPR certification; must pass criminal background check; must pass abuse registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://inhomecare.wv.gov/providers/Pages/Requirements.aspx',
                'phone': '(304) 558-0050',
                'email': 'ohflac@wv.gov'
            },
            {
                'state': west_virginia,
                'program_name': 'Other HCBS Waivers',
                'administering_agency': 'West Virginia Department of Health and Human Resources (DHHR), Office of Health Facility Licensure and Certification',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (federal minimum for HHA certification; required in WV); must complete 16 clinical hours (hands-on, supervised); must pass state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must be at least 18 years old; must have CPR certification; must pass criminal background check; must pass abuse registry check',
                'annual_training_requirements': 'Abuse/neglect/exploitation and dementia training required for registration renewal; OSHA and HIPAA training required for registration renewal; First aid training required for registration renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'West Virginia In-Home Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of training; must complete 16 clinical hours; must pass state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must be at least 18 years old; must have CPR certification; must pass criminal background check; must pass abuse registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://inhomecare.wv.gov/providers/Pages/Requirements.aspx',
                'phone': '(304) 558-0050',
                'email': 'ohflac@wv.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated West Virginia waiver programs')) 