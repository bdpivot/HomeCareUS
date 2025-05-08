from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Nevada waiver programs'

    def handle(self, *args, **kwargs):
        nevada = State.objects.get(abbreviation='NV')
        
        waiver_programs = [
            {
                'state': nevada,
                'program_name': 'Nevada Medicaid Home Health Services',
                'administering_agency': 'Nevada Department of Health and Human Services, Division of Public and Behavioral Health (DPBH), Bureau of Health Care Quality & Compliance',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; home health agencies must provide skilled nursing and cannot exist solely for HHA services; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nevada State Board of Nursing Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment, Business License Application',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written and clinical competency evaluation, be at least 18 years old, have good communication and literacy skills, be responsible and mature, pass criminal background check, and be certified at the CNA level by the Board of Nursing',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dpbh.nv.gov/Reg/HealthFacilities/dta/Licensing/Health_Facilities_-_Licensing/',
                'phone': '(702) 486-6515',
                'email': 'hfl@health.nv.gov'
            },
            {
                'state': nevada,
                'program_name': 'Personal Care Services (PCS) Program',
                'administering_agency': 'Nevada Department of Health and Human Services, Division of Public and Behavioral Health (DPBH)',
                'services_offered': 'ADLs (bathing, dressing, grooming, toileting, mobility, eating) and IADLs (meal prep, housekeeping, laundry, shopping)',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; personal care agencies have lower requirements (8 hours annual training, 18+, basic skills)',
                'annual_training_requirements': '8 hours annual training required for personal care agency attendants',
                'effective_date': '2024-01-01',
                'registry_name': 'Nevada State Board of Nursing Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for PCS, Level of Care Assessment, Financial Assessment, Business License Application',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written and clinical competency evaluation, be at least 18 years old, have good communication and literacy skills, be responsible and mature, pass criminal background check, and be certified at the CNA level by the Board of Nursing',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.leg.state.nv.us/App/InterimCommittee/REL/Document/2586',
                'phone': '(702) 486-6515',
                'email': 'hfl@health.nv.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Nevada waiver programs')) 