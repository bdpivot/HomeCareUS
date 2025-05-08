from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Louisiana waiver programs'

    def handle(self, *args, **kwargs):
        louisiana = State.objects.get(abbreviation='LA')
        
        waiver_programs = [
            {
                'state': louisiana,
                'program_name': 'Healthy Louisiana (Medicaid Managed Care)',
                'administering_agency': 'Louisiana Department of Health (LDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Louisiana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Healthy Louisiana, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training or be a CNA, pass competency exam, pass background check, have high school diploma or GED, and have physical exam',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'LDH Training Portal, State-approved HHA training programs',
                'website': 'https://ldh.la.gov/health-standards-section/home-health',
                'phone': '(225) 342-0138',
                'email': 'hssinfo@la.gov'
            },
            {
                'state': louisiana,
                'program_name': 'Community Choices Waiver (CCW)',
                'administering_agency': 'Louisiana Department of Health (LDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be senior/adult with disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Louisiana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CCW, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training or be a CNA, pass competency exam, pass background check, have high school diploma or GED, and have physical exam',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'LDH Training Portal, State-approved HHA training programs',
                'website': 'https://ldh.la.gov/health-standards-section/home-and-community-based-service-providers-hcbs',
                'phone': '(225) 342-0138',
                'email': 'hssinfo@la.gov'
            },
            {
                'state': louisiana,
                'program_name': 'Long Term-Personal Care Services (LT-PCS)',
                'administering_agency': 'Louisiana Department of Health (LDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Louisiana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for LT-PCS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training or be a CNA, pass competency exam, pass background check, have high school diploma or GED, and have physical exam',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'LDH Training Portal, State-approved HHA training programs',
                'website': 'https://ldh.la.gov/health-standards-section/home-and-community-based-service-providers-hcbs',
                'phone': '(225) 342-0138',
                'email': 'hssinfo@la.gov'
            },
            {
                'state': louisiana,
                'program_name': 'Monitored In-Home Caregiving (MIHC)',
                'administering_agency': 'Louisiana Department of Health (LDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Louisiana Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MIHC, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training or be a CNA, pass competency exam, pass background check, have high school diploma or GED, and have physical exam',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'LDH Training Portal, State-approved HHA training programs',
                'website': 'https://ldh.la.gov/health-standards-section/home-and-community-based-service-providers-hcbs',
                'phone': '(225) 342-0138',
                'email': 'hssinfo@la.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Louisiana waiver programs')) 