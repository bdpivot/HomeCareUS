from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Wisconsin waiver programs'

    def handle(self, *args, **kwargs):
        wisconsin = State.objects.get(abbreviation='WI')
        
        waiver_programs = [
            {
                'state': wisconsin,
                'program_name': 'Wisconsin Medicaid Home Health Services',
                'administering_agency': 'Wisconsin Department of Health Services (DHS), Division of Quality Assurance',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 120 total hours (state requirement for HHA/CNA certification; exceeds federal minimum); must complete 32 clinical hours (hands-on, supervised); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wisconsin Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours of training; must complete 32 clinical hours; must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dhs.wisconsin.gov/regulations/home-health.htm',
                'phone': '(608) 266-8481',
                'email': 'dhsqualityassurance@dhs.wisconsin.gov'
            },
            {
                'state': wisconsin,
                'program_name': 'Family Care Waiver',
                'administering_agency': 'Wisconsin Department of Health Services (DHS), Division of Quality Assurance',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 120 total hours (state requirement for HHA/CNA certification; exceeds federal minimum); must complete 32 clinical hours (hands-on, supervised); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wisconsin Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Family Care Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours of training; must complete 32 clinical hours; must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dhs.wisconsin.gov/familycare/index.htm',
                'phone': '(608) 266-8481',
                'email': 'dhsqualityassurance@dhs.wisconsin.gov'
            },
            {
                'state': wisconsin,
                'program_name': 'Include, Respect, I Self-Direct (IRIS) Waiver',
                'administering_agency': 'Wisconsin Department of Health Services (DHS), Division of Quality Assurance',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 120 total hours (state requirement for HHA/CNA certification; exceeds federal minimum); must complete 32 clinical hours (hands-on, supervised); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wisconsin Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for IRIS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours of training; must complete 32 clinical hours; must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dhs.wisconsin.gov/iris/index.htm',
                'phone': '(608) 266-8481',
                'email': 'dhsqualityassurance@dhs.wisconsin.gov'
            },
            {
                'state': wisconsin,
                'program_name': 'Partnership Waiver',
                'administering_agency': 'Wisconsin Department of Health Services (DHS), Division of Quality Assurance',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 120 total hours (state requirement for HHA/CNA certification; exceeds federal minimum); must complete 32 clinical hours (hands-on, supervised); must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'annual_training_requirements': '12 hours annual in-service/continuing education',
                'effective_date': '2024-01-01',
                'registry_name': 'Wisconsin Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Partnership Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours of training; must complete 32 clinical hours; must pass state-approved CNA/HHA training program; must pass written and skills competency exam; must be at least 16 years old; must have high school diploma or GED (recommended by most employers); must be listed on the Wisconsin Nurse Aide Registry; must pass criminal background check; must pass abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dhs.wisconsin.gov/partnership/index.htm',
                'phone': '(608) 266-8481',
                'email': 'dhsqualityassurance@dhs.wisconsin.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Wisconsin waiver programs')) 