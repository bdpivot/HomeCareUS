from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Maine waiver programs'

    def handle(self, *args, **kwargs):
        maine = State.objects.get(abbreviation='ME')
        
        waiver_programs = [
            {
                'state': maine,
                'program_name': 'MaineCare Home Health Services',
                'administering_agency': 'Maine Department of Health and Human Services (DHHS), Division of Licensing and Certification',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maine Registry of Certified Nursing Assistants & Direct Care Workers',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MaineCare Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 180 total hours (90 theory, 20 lab, 70 clinical) of state-approved HHA training, pass Maine HHA certification exam, pass background check, have minimum 9th-grade education, be at least 16 years old, and be listed on Maine Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'DHHS Training Portal, State-approved HHA training programs',
                'website': 'https://www.maine.gov/dhhs/dlc/cna-registry',
                'phone': '(207) 287-9300',
                'email': 'dhhs@maine.gov'
            },
            {
                'state': maine,
                'program_name': 'Home and Community Benefits (HCB) Waiver for the Elderly and Adults with Disabilities',
                'administering_agency': 'Maine Department of Health and Human Services (DHHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, assistive technology, emergency response systems',
                'unique_requirements': 'Must be elderly/adult with disability at risk of nursing facility placement, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maine Registry of Certified Nursing Assistants & Direct Care Workers',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCB Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 180 total hours (90 theory, 20 lab, 70 clinical) of state-approved HHA training, pass Maine HHA certification exam, pass background check, have minimum 9th-grade education, be at least 16 years old, and be listed on Maine Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'DHHS Training Portal, State-approved HHA training programs',
                'website': 'https://www.maine.gov/dhhs/dlc/cna-registry',
                'phone': '(207) 287-9300',
                'email': 'dhhs@maine.gov'
            },
            {
                'state': maine,
                'program_name': 'Personal Care Attendant (PCA) Services',
                'administering_agency': 'Maine Department of Health and Human Services (DHHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maine Registry of Certified Nursing Assistants & Direct Care Workers',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for PCA Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 180 total hours (90 theory, 20 lab, 70 clinical) of state-approved HHA training, pass Maine HHA certification exam, pass background check, have minimum 9th-grade education, be at least 16 years old, and be listed on Maine Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'DHHS Training Portal, State-approved HHA training programs',
                'website': 'https://www.maine.gov/dhhs/dlc/cna-registry',
                'phone': '(207) 287-9300',
                'email': 'dhhs@maine.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Maine waiver programs')) 