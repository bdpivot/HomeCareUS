from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Virginia waiver programs'

    def handle(self, *args, **kwargs):
        virginia = State.objects.get(abbreviation='VA')
        
        waiver_programs = [
            {
                'state': virginia,
                'program_name': 'Commonwealth Coordinated Care (CCC) Plus Waiver',
                'administering_agency': 'Virginia Department of Medical Assistance Services (DMAS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and environmental modifications',
                'unique_requirements': 'Must complete 75 total hours (minimum required for HHA certification; must include at least 16 clinical hours); must pass state-approved HHA training program (classroom and hands-on clinical); must pass certification exam; must be listed on the Virginia Nurse Aide Registry; must have high school diploma or GED; must be at least 18 years old (unless certified as a nurse aide); must pass criminal background check; must have valid driver\'s license and reliable transportation; must be physically able to perform aide duties',
                'annual_training_requirements': 'Annual training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency',
                'effective_date': '2024-01-01',
                'registry_name': 'Virginia Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CCC Plus Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of training; must pass state-approved HHA training program; must pass certification exam; must be listed on the Virginia Nurse Aide Registry; must have high school diploma or GED; must be at least 18 years old; must pass criminal background check; must have valid driver\'s license and reliable transportation',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dmas.virginia.gov/for-members/archive/waivers/',
                'phone': '(804) 786-7933',
                'email': 'dmasinfo@dmas.virginia.gov'
            },
            {
                'state': virginia,
                'program_name': 'Developmental Disability (DD) Waivers',
                'administering_agency': 'Virginia Department of Medical Assistance Services (DMAS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and environmental modifications',
                'unique_requirements': 'Must complete 75 total hours (minimum required for HHA certification; must include at least 16 clinical hours); must pass state-approved HHA training program (classroom and hands-on clinical); must pass certification exam; must be listed on the Virginia Nurse Aide Registry; must have high school diploma or GED; must be at least 18 years old (unless certified as a nurse aide); must pass criminal background check; must have valid driver\'s license and reliable transportation; must be physically able to perform aide duties',
                'annual_training_requirements': 'Annual training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency',
                'effective_date': '2024-01-01',
                'registry_name': 'Virginia Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for DD Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of training; must pass state-approved HHA training program; must pass certification exam; must be listed on the Virginia Nurse Aide Registry; must have high school diploma or GED; must be at least 18 years old; must pass criminal background check; must have valid driver\'s license and reliable transportation',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dmas.virginia.gov/for-members/archive/waivers/',
                'phone': '(804) 786-7933',
                'email': 'dmasinfo@dmas.virginia.gov'
            },
            {
                'state': virginia,
                'program_name': 'Virginia Medicaid Home Health Services',
                'administering_agency': 'Virginia Department of Medical Assistance Services (DMAS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and environmental modifications',
                'unique_requirements': 'Must complete 75 total hours (minimum required for HHA certification; must include at least 16 clinical hours); must pass state-approved HHA training program (classroom and hands-on clinical); must pass certification exam; must be listed on the Virginia Nurse Aide Registry; must have high school diploma or GED; must be at least 18 years old (unless certified as a nurse aide); must pass criminal background check; must have valid driver\'s license and reliable transportation; must be physically able to perform aide duties',
                'annual_training_requirements': 'Annual training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency',
                'effective_date': '2024-01-01',
                'registry_name': 'Virginia Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours of training; must pass state-approved HHA training program; must pass certification exam; must be listed on the Virginia Nurse Aide Registry; must have high school diploma or GED; must be at least 18 years old; must pass criminal background check; must have valid driver\'s license and reliable transportation',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dmas.virginia.gov/for-members/archive/waivers/',
                'phone': '(804) 786-7933',
                'email': 'dmasinfo@dmas.virginia.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Virginia waiver programs')) 