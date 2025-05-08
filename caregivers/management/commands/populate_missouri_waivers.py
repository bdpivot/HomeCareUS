from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Missouri waiver programs'

    def handle(self, *args, **kwargs):
        missouri = State.objects.get(abbreviation='MO')
        
        waiver_programs = [
            {
                'state': missouri,
                'program_name': 'MO HealthNet (Missouri Medicaid) Home Health Services',
                'administering_agency': 'Missouri Department of Health and Senior Services (DHSS), Bureau of Home Care and Rehabilitative Standards',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; agency must offer at least two skilled services, one of which must be skilled nursing',
                'annual_training_requirements': '12 hours annual in-service/continuing education required; dementia-specific training required for direct care workers with dementia patients',
                'effective_date': '2024-01-01',
                'registry_name': 'Missouri Family Care Safety Registry (FCSR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MO HealthNet Home Health, Level of Care Assessment, Financial Assessment, State Disclosure of Ownership and Control Interest Statement',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass HHA competency evaluation (written and clinical skills), have high school diploma or equivalent, be at least 18 years old, pass criminal background check and Family Care Safety Registry check, and be listed on Missouri Family Care Safety Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.mo.gov/safety/homecare/',
                'phone': '(573) 751-6303',
                'email': 'info@health.mo.gov'
            },
            {
                'state': missouri,
                'program_name': 'Aged & Disabled Waiver (ADW)',
                'administering_agency': 'Missouri Division of Aging',
                'services_offered': 'Personal care, homemaker services, home-delivered meals, adult day care, respite care',
                'unique_requirements': 'Must be 63+ years old, at risk of institutionalization, meet nursing home level of care, and have income below 300% of SSI; agency-based care only (no participant direction)',
                'annual_training_requirements': '12 hours annual in-service/continuing education required; dementia-specific training required for direct care workers with dementia patients',
                'effective_date': '2024-01-01',
                'registry_name': 'Missouri Family Care Safety Registry (FCSR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for ADW, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass HHA competency evaluation (written and clinical skills), have high school diploma or equivalent, be at least 18 years old, pass criminal background check and Family Care Safety Registry check, and be listed on Missouri Family Care Safety Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.mo.gov/safety/homecare/',
                'phone': '(573) 751-6303',
                'email': 'info@health.mo.gov'
            },
            {
                'state': missouri,
                'program_name': 'Home and Community Based Services (HCBS)',
                'administering_agency': 'Missouri Department of Health and Senior Services (DHSS)',
                'services_offered': 'Personal care, homemaker services, home-delivered meals, adult day care, respite care',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; waitlist may apply',
                'annual_training_requirements': '12 hours annual in-service/continuing education required; dementia-specific training required for direct care workers with dementia patients',
                'effective_date': '2024-01-01',
                'registry_name': 'Missouri Family Care Safety Registry (FCSR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass HHA competency evaluation (written and clinical skills), have high school diploma or equivalent, be at least 18 years old, pass criminal background check and Family Care Safety Registry check, and be listed on Missouri Family Care Safety Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.mo.gov/safety/homecare/',
                'phone': '(573) 751-6303',
                'email': 'info@health.mo.gov'
            },
            {
                'state': missouri,
                'program_name': 'Consumer Directed Services (CDS)',
                'administering_agency': 'Missouri Department of Health and Senior Services (DHSS)',
                'services_offered': 'Personal care, homemaker services, respite care',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; participant selects, trains, and manages caregiver (including family/friends, except spouse or legal guardian)',
                'annual_training_requirements': '12 hours annual in-service/continuing education required; dementia-specific training required for direct care workers with dementia patients',
                'effective_date': '2024-01-01',
                'registry_name': 'Missouri Family Care Safety Registry (FCSR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CDS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass HHA competency evaluation (written and clinical skills), have high school diploma or equivalent, be at least 18 years old, pass criminal background check and Family Care Safety Registry check, and be listed on Missouri Family Care Safety Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': False,
                'salary_range_min': 13.50,
                'salary_range_max': 18.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.mo.gov/safety/homecare/',
                'phone': '(573) 751-6303',
                'email': 'info@health.mo.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Missouri waiver programs')) 