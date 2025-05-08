from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Montana waiver programs'

    def handle(self, *args, **kwargs):
        montana = State.objects.get(abbreviation='MT')
        
        waiver_programs = [
            {
                'state': montana,
                'program_name': 'Montana Medicaid Home Health Services',
                'administering_agency': 'Montana Department of Public Health and Human Services (DPHHS), Quality Assurance Division',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Ongoing education required to maintain registry status',
                'effective_date': '2024-01-01',
                'registry_name': 'Montana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment, BOUNDS portal registration',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must first hold a Montana CNA Certificate, complete 91 classroom and 25 clinical hours of state-approved HHA training, pass Montana HHA certification exam, have high school diploma or equivalent, pass criminal background check, and be registered with Montana Nurse Aide Registry with HHA endorsement',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dphhs.mt.gov/qad/licensure/healthcarefacilitylicensure/lbfacilityapplications/lbhomehealthagency',
                'phone': '(406) 444-2676',
                'email': 'qad@mt.gov'
            },
            {
                'state': montana,
                'program_name': 'Big Sky Waiver',
                'administering_agency': 'Montana Department of Public Health and Human Services (DPHHS)',
                'services_offered': 'Personal care, respite care, homemaker services, skilled nursing',
                'unique_requirements': 'Must be elderly or adult with disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': 'Ongoing education required to maintain registry status',
                'effective_date': '2024-01-01',
                'registry_name': 'Montana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Big Sky Waiver, Level of Care Assessment, Financial Assessment, BOUNDS portal registration',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must first hold a Montana CNA Certificate, complete 91 classroom and 25 clinical hours of state-approved HHA training, pass Montana HHA certification exam, have high school diploma or equivalent, pass criminal background check, and be registered with Montana Nurse Aide Registry with HHA endorsement',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dphhs.mt.gov/sltc/homehealthpolicymanual',
                'phone': '(406) 444-2676',
                'email': 'qad@mt.gov'
            },
            {
                'state': montana,
                'program_name': 'Home and Community Based Services (HCBS) Waivers',
                'administering_agency': 'Montana Department of Public Health and Human Services (DPHHS)',
                'services_offered': 'Personal care, respite care, homemaker services, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Ongoing education required to maintain registry status',
                'effective_date': '2024-01-01',
                'registry_name': 'Montana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment, BOUNDS portal registration',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must first hold a Montana CNA Certificate, complete 91 classroom and 25 clinical hours of state-approved HHA training, pass Montana HHA certification exam, have high school diploma or equivalent, pass criminal background check, and be registered with Montana Nurse Aide Registry with HHA endorsement',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dphhs.mt.gov/sltc/homehealthpolicymanual',
                'phone': '(406) 444-2676',
                'email': 'qad@mt.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Montana waiver programs')) 