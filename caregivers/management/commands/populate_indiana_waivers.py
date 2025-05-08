from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Indiana waiver programs'

    def handle(self, *args, **kwargs):
        indiana = State.objects.get(abbreviation='IN')
        
        waiver_programs = [
            {
                'state': indiana,
                'program_name': 'Indiana Medicaid Home Health Services',
                'administering_agency': 'Indiana Department of Health (IDOH), Home Health Aide Registration Program',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Indiana Aides Registry (IDOH)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency exam, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'IDOH Training Portal, Agency-based training programs',
                'website': 'https://www.in.gov/health/ltc/aide-training-and-certification/hha/',
                'phone': '(317) 233-7442',
                'email': 'hha@health.in.gov'
            },
            {
                'state': indiana,
                'program_name': 'Aged and Disabled (A&D) Waiver',
                'administering_agency': 'Indiana Department of Health (IDOH), Home Health Aide Registration Program',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be elderly or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Indiana Aides Registry (IDOH)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for A&D Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'IDOH Training Portal, Agency-based training programs',
                'website': 'https://www.in.gov/health/ltc/aide-training-and-certification/hha/',
                'phone': '(317) 233-7442',
                'email': 'hha@health.in.gov'
            },
            {
                'state': indiana,
                'program_name': 'Traumatic Brain Injury (TBI) Waiver',
                'administering_agency': 'Indiana Department of Health (IDOH), Home Health Aide Registration Program',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must have traumatic brain injury, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Indiana Aides Registry (IDOH)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for TBI Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'IDOH Training Portal, Agency-based training programs',
                'website': 'https://www.in.gov/health/ltc/aide-training-and-certification/hha/',
                'phone': '(317) 233-7442',
                'email': 'hha@health.in.gov'
            },
            {
                'state': indiana,
                'program_name': 'Community Integration and Habilitation (CIH) Waiver',
                'administering_agency': 'Indiana Department of Health (IDOH), Home Health Aide Registration Program',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must have developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Indiana Aides Registry (IDOH)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CIH Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'IDOH Training Portal, Agency-based training programs',
                'website': 'https://www.in.gov/health/ltc/aide-training-and-certification/hha/',
                'phone': '(317) 233-7442',
                'email': 'hha@health.in.gov'
            },
            {
                'state': indiana,
                'program_name': 'Family Supports Waiver',
                'administering_agency': 'Indiana Department of Health (IDOH), Home Health Aide Registration Program',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must have developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Indiana Aides Registry (IDOH)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Family Supports Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'IDOH Training Portal, Agency-based training programs',
                'website': 'https://www.in.gov/health/ltc/aide-training-and-certification/hha/',
                'phone': '(317) 233-7442',
                'email': 'hha@health.in.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Indiana waiver programs')) 