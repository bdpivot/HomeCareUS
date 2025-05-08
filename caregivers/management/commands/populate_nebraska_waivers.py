from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Nebraska waiver programs'

    def handle(self, *args, **kwargs):
        nebraska = State.objects.get(abbreviation='NE')
        
        waiver_programs = [
            {
                'state': nebraska,
                'program_name': 'Nebraska Medicaid Home Health Services',
                'administering_agency': 'Nebraska Department of Health and Human Services (DHHS), Division of Public Health, Licensure Unit',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nebraska Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved nurse aide or home health aide training, pass written and clinical competency evaluation (minimum 70%), have high school diploma or GED (recommended), be at least 16 years old, speak and understand English or a language understood by a substantial portion of the healthcare population, have no convictions involving moral turpitude, pass criminal background check, and be listed on the Nebraska Nurse Aide Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dhhs.ne.gov/licensure/Pages/Home-Health-Agencies.aspx',
                'phone': '(402) 471-2115',
                'email': 'dhhs.licensureunit@nebraska.gov'
            },
            {
                'state': nebraska,
                'program_name': 'Home and Community-Based Services (HCBS) Waivers',
                'administering_agency': 'Nebraska Department of Health and Human Services (DHHS)',
                'services_offered': 'Personal care, respite care, homemaker services',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must work as a nurse aide in a paid position within 24 months to stay active on the registry',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nebraska Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved nurse aide or home health aide training, pass written and clinical competency evaluation (minimum 70%), have high school diploma or GED (recommended), be at least 16 years old, speak and understand English or a language understood by a substantial portion of the healthcare population, have no convictions involving moral turpitude, pass criminal background check, and be listed on the Nebraska Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.50,
                'salary_range_max': 18.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dhhs.ne.gov/licensure/Pages/Nurse-Aide-Requirements.aspx',
                'phone': '(402) 471-2115',
                'email': 'dhhs.licensureunit@nebraska.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Nebraska waiver programs')) 