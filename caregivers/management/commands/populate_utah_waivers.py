from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Utah waiver programs'

    def handle(self, *args, **kwargs):
        utah = State.objects.get(abbreviation='UT')
        
        waiver_programs = [
            {
                'state': utah,
                'program_name': 'Utah Medicaid Home Health Services',
                'administering_agency': 'Utah Department of Health and Human Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must complete 75 total hours of state-approved HHA training program; must pass written and clinical competency exam administered by Utah Department of Health; must be at least 18 years old; must have high school diploma or GED; competency exams in reading, English, and math may be required; must pass criminal background check; must pass tuberculosis (TB) skin test; must pass physical exam; must demonstrate competency in basic health and safety protocols; personal care aides in Level II assisted living must be CNA or pursuing CNA status',
                'annual_training_requirements': '12 hours annual in-service/continuing education recommended for career advancement',
                'effective_date': '2024-01-01',
                'registry_name': 'Utah Nursing Assistant Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Utah Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours of state-approved HHA training program; must pass written and clinical competency exam; must be at least 18 years old; must have high school diploma or GED; must pass criminal background check; must pass tuberculosis (TB) skin test; must pass physical exam',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://medicaid.utah.gov/statewide-medicaid-provider-training-utah/',
                'phone': '(801) 538-6155',
                'email': 'medicaid@utah.gov'
            },
            {
                'state': utah,
                'program_name': 'Aging Waiver (Utah Waiver for Individuals Age 65 or Older, 1915(c) HCBS)',
                'administering_agency': 'Utah Department of Health and Human Services',
                'services_offered': 'Personal care, respite, home modifications, and emergency response',
                'unique_requirements': 'Must complete 75 total hours of state-approved HHA training program; must pass written and clinical competency exam administered by Utah Department of Health; must be at least 18 years old; must have high school diploma or GED; competency exams in reading, English, and math may be required; must pass criminal background check; must pass tuberculosis (TB) skin test; must pass physical exam; must demonstrate competency in basic health and safety protocols; personal care aides in Level II assisted living must be CNA or pursuing CNA status',
                'annual_training_requirements': '12 hours annual in-service/continuing education recommended for career advancement',
                'effective_date': '2024-01-01',
                'registry_name': 'Utah Nursing Assistant Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Aging Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of state-approved HHA training program; must pass written and clinical competency exam; must be at least 18 years old; must have high school diploma or GED; must pass criminal background check; must pass tuberculosis (TB) skin test; must pass physical exam; in some cases, even a spouse may be hired',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://medicaid.utah.gov/statewide-medicaid-provider-training-utah/',
                'phone': '(801) 538-6155',
                'email': 'aging@utah.gov'
            },
            {
                'state': utah,
                'program_name': 'Other Home and Community-Based Services (HCBS) Waivers',
                'administering_agency': 'Utah Department of Health and Human Services',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and home modifications',
                'unique_requirements': 'Must complete 75 total hours of state-approved HHA training program; must pass written and clinical competency exam administered by Utah Department of Health; must be at least 18 years old; must have high school diploma or GED; competency exams in reading, English, and math may be required; must pass criminal background check; must pass tuberculosis (TB) skin test; must pass physical exam; must demonstrate competency in basic health and safety protocols; personal care aides in Level II assisted living must be CNA or pursuing CNA status',
                'annual_training_requirements': '12 hours annual in-service/continuing education recommended for career advancement',
                'effective_date': '2024-01-01',
                'registry_name': 'Utah Nursing Assistant Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of state-approved HHA training program; must pass written and clinical competency exam; must be at least 18 years old; must have high school diploma or GED; must pass criminal background check; must pass tuberculosis (TB) skin test; must pass physical exam; in some cases, even a spouse may be hired',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://medicaid.utah.gov/statewide-medicaid-provider-training-utah/',
                'phone': '(801) 538-6155',
                'email': 'hcbs@utah.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Utah waiver programs')) 