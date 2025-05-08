from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Michigan waiver programs'

    def handle(self, *args, **kwargs):
        michigan = State.objects.get(abbreviation='MI')
        
        waiver_programs = [
            {
                'state': michigan,
                'program_name': 'Michigan Medicaid Home Health Services',
                'administering_agency': 'Michigan Department of Licensing and Regulatory Affairs (LARA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Michigan Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written competency exam, pass background check and drug screening, have high school diploma or GED, and be listed on Michigan Nurse Aide Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'LARA Training Portal, State-approved HHA training programs',
                'website': 'https://www.michigan.gov/lara/bureau-list/bsc/accs-division/hha',
                'phone': '(517) 335-1980',
                'email': 'lara-hha@michigan.gov'
            },
            {
                'state': michigan,
                'program_name': 'MI Choice Waiver Program',
                'administering_agency': 'Michigan Department of Health and Human Services (MDHHS)',
                'services_offered': 'Personal care, respite care, environmental modifications, home-delivered meals, supports coordination',
                'unique_requirements': 'Must be senior or adult with disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Michigan Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MI Choice Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written competency exam, pass background check and drug screening, have high school diploma or GED, and be listed on Michigan Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.50,
                'salary_range_max': 18.50,
                'free_training_available': True,
                'free_training_programs': 'LARA Training Portal, State-approved HHA training programs',
                'website': 'https://www.michigan.gov/mdhhs/assistance-programs/medicaid/portalhome/medicaid-providers/training',
                'phone': '(517) 241-3740',
                'email': 'mdhhs-mi-choice@michigan.gov'
            },
            {
                'state': michigan,
                'program_name': 'Home Help Program',
                'administering_agency': 'Michigan Department of Health and Human Services (MDHHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; no waitlist',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Michigan Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Home Help Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written competency exam, pass background check and drug screening, have high school diploma or GED, and be listed on Michigan Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'LARA Training Portal, State-approved HHA training programs',
                'website': 'https://www.michigan.gov/mdhhs/assistance-programs/medicaid/portalhome/medicaid-providers/training',
                'phone': '(517) 241-3740',
                'email': 'mdhhs-home-help@michigan.gov'
            },
            {
                'state': michigan,
                'program_name': 'MI Health Link',
                'administering_agency': 'Michigan Department of Health and Human Services (MDHHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, care coordination',
                'unique_requirements': 'Must be dual-eligible for Medicare and Medicaid, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Michigan Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MI Health Link, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written competency exam, pass background check and drug screening, have high school diploma or GED, and be listed on Michigan Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'LARA Training Portal, State-approved HHA training programs',
                'website': 'https://www.michigan.gov/mdhhs/assistance-programs/medicaid/portalhome/medicaid-providers/training',
                'phone': '(517) 241-3740',
                'email': 'mdhhs-mi-health-link@michigan.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Michigan waiver programs')) 