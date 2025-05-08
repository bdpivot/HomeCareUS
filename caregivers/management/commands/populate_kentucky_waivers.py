from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Kentucky waiver programs'

    def handle(self, *args, **kwargs):
        kentucky = State.objects.get(abbreviation='KY')
        
        waiver_programs = [
            {
                'state': kentucky,
                'program_name': 'Kentucky Medicaid Home Health Services',
                'administering_agency': 'Kentucky Cabinet for Health and Family Services (CHFS), Office of Inspector General (OIG)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kentucky Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, and be listed on Kentucky Nurse Aide Registry as SRNA',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'Kentucky Community and Technical College System (KCTCS), State-approved HHA training programs',
                'website': 'https://chfs.ky.gov/agencies/dail/pages/homecare.aspx',
                'phone': '(502) 564-7963',
                'email': 'chfs.webmaster@ky.gov'
            },
            {
                'state': kentucky,
                'program_name': 'Home and Community Based (HCB) Waiver',
                'administering_agency': 'Kentucky Cabinet for Health and Family Services (CHFS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be elderly/disabled at risk of nursing facility placement, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kentucky Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCB Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, and be listed on Kentucky Nurse Aide Registry as SRNA',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'Kentucky Community and Technical College System (KCTCS), State-approved HHA training programs',
                'website': 'https://chfs.ky.gov/agencies/dms/dca/Pages/HCBSWaiver.aspx',
                'phone': '(502) 564-7963',
                'email': 'chfs.webmaster@ky.gov'
            },
            {
                'state': kentucky,
                'program_name': 'Money Follows the Person (MFP) Program',
                'administering_agency': 'Kentucky Cabinet for Health and Family Services (CHFS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be transitioning from nursing home to community, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kentucky Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MFP Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, and be listed on Kentucky Nurse Aide Registry as SRNA',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'Kentucky Community and Technical College System (KCTCS), State-approved HHA training programs',
                'website': 'https://chfs.ky.gov/agencies/dms/dca/Pages/HCBSWaiver.aspx',
                'phone': '(502) 564-7963',
                'email': 'chfs.webmaster@ky.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Kentucky waiver programs')) 