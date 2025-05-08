from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Arkansas waiver programs'

    def handle(self, *args, **kwargs):
        arkansas = State.objects.get(abbreviation='AR')
        
        waiver_programs = [
            {
                'state': arkansas,
                'program_name': 'ARChoices in Homecare',
                'administering_agency': 'Arkansas Department of Human Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, Personal Emergency Response Systems (PERS)',
                'unique_requirements': 'Must be 65 or older or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency-maintained records (no statewide registry)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for ARChoices, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) for HHA or 40 hours for Personal Care Aide, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 10.00,
                'salary_range_max': 15.00,
                'free_training_available': True,
                'free_training_programs': 'Arkansas DHS Training Portal, Agency-based training programs',
                'website': 'https://humanservices.arkansas.gov/divisions-shared-services/medical-services/programs/archoices/',
                'phone': '(501) 682-1001',
                'email': 'archoices@dhs.arkansas.gov'
            },
            {
                'state': arkansas,
                'program_name': 'Independent Choices',
                'administering_agency': 'Arkansas Department of Human Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be 65 or older or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency-maintained records (no statewide registry)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Independent Choices, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Participant can hire, train, and manage caregiver of their choosing (excluding spouse/guardian), must pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': False,
                'salary_range_min': 10.50,
                'salary_range_max': 15.50,
                'free_training_available': True,
                'free_training_programs': 'Arkansas DHS Training Portal, Participant-directed training',
                'website': 'https://humanservices.arkansas.gov/divisions-shared-services/medical-services/programs/independent-choices/',
                'phone': '(501) 682-1001',
                'email': 'independent.choices@dhs.arkansas.gov'
            },
            {
                'state': arkansas,
                'program_name': 'Personal Care Services (Medicaid State Plan)',
                'administering_agency': 'Arkansas Department of Human Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency-maintained records (no statewide registry)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Personal Care Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 40 hours minimum for Personal Care Aide, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 10.25,
                'salary_range_max': 15.25,
                'free_training_available': True,
                'free_training_programs': 'Arkansas DHS Training Portal, Agency-based training programs',
                'website': 'https://humanservices.arkansas.gov/divisions-shared-services/medical-services/programs/personal-care/',
                'phone': '(501) 682-1001',
                'email': 'personal.care@dhs.arkansas.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Arkansas waiver programs')) 