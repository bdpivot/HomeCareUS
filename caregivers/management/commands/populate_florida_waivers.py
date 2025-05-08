from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Florida waiver programs'

    def handle(self, *args, **kwargs):
        florida = State.objects.get(abbreviation='FL')
        
        waiver_programs = [
            {
                'state': florida,
                'program_name': 'Statewide Medicaid Managed Care (SMMC) – Long-Term Care (LTC) Program',
                'administering_agency': 'Florida Agency for Health Care Administration (AHCA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required (includes HIV/AIDS and CPR)',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for SMMC-LTC, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) for Medicare/Medicaid agencies or 40 hours for state-licensed-only agencies, pass AHCA-approved competency test, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'AHCA Training Portal, State-approved HHA training programs',
                'website': 'https://ahca.myflorida.com/medicaid/medicaid-policy-and-quality/medicaid-policy/federal-authorities/federal-waivers/florida-medicaid-s-covered-services-and-waivers',
                'phone': '(850) 412-4000',
                'email': 'ahca.medicaid@ahca.myflorida.com'
            },
            {
                'state': florida,
                'program_name': 'iBudget Waiver',
                'administering_agency': 'Agency for Persons with Disabilities (APD)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must have developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required (includes HIV/AIDS and CPR)',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for iBudget, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) for Medicare/Medicaid agencies or 40 hours for state-licensed-only agencies, pass AHCA-approved competency test, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'AHCA Training Portal, State-approved HHA training programs',
                'website': 'https://apd.myflorida.com/providers/ibudget/',
                'phone': '(850) 488-4257',
                'email': 'apd.ibudget@apdcares.org'
            },
            {
                'state': florida,
                'program_name': 'Consumer Directed Care Plus (CDC+)',
                'administering_agency': 'Florida Agency for Health Care Administration (AHCA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required (includes HIV/AIDS and CPR)',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CDC+, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) for Medicare/Medicaid agencies or 40 hours for state-licensed-only agencies, pass AHCA-approved competency test, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': False,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'AHCA Training Portal, State-approved HHA training programs',
                'website': 'https://ahca.myflorida.com/medicaid/medicaid-policy-and-quality/medicaid-policy/federal-authorities/federal-waivers/florida-medicaid-s-covered-services-and-waivers',
                'phone': '(850) 412-4000',
                'email': 'ahca.cdcplus@ahca.myflorida.com'
            },
            {
                'state': florida,
                'program_name': 'Home Health Aide for Medically Fragile Children (HHAMFC) Program',
                'administering_agency': 'Florida Agency for Health Care Administration (AHCA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be medically fragile child, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required (includes HIV/AIDS and CPR)',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HHAMFC, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 86-hour program (40 hours theory, 30 hours skills, 16 hours clinical), pass AHCA-approved competency test, pass background check, and be 18 years or older',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'AHCA Training Portal, State-approved HHA training programs',
                'website': 'https://ahca.myflorida.com/medicaid/medicaid-policy-and-quality/medicaid-policy/federal-authorities/federal-waivers/florida-medicaid-s-covered-services-and-waivers',
                'phone': '(850) 412-4000',
                'email': 'ahca.hhamfc@ahca.myflorida.com'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Florida waiver programs')) 