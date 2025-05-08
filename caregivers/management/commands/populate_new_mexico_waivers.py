from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates New Mexico waiver programs'

    def handle(self, *args, **kwargs):
        new_mexico = State.objects.get(abbreviation='NM')
        
        waiver_programs = [
            {
                'state': new_mexico,
                'program_name': 'Centennial Care (New Mexico Medicaid Managed Care)',
                'administering_agency': 'New Mexico Department of Health (DOH), Division of Health Improvement',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'New Mexico Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written and skills competency evaluation, be at least 18 years old, have high school diploma or GED (required by most employers), pass background check before employment/certification, and undergo annual performance review by agency',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.hsd.state.nm.us/centennial-care/',
                'phone': '(505) 827-3100',
                'email': 'centennial.care@state.nm.us'
            },
            {
                'state': new_mexico,
                'program_name': 'Mi Via Waiver',
                'administering_agency': 'New Mexico Department of Health (DOH), Division of Health Improvement',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; self-directed, 1915(c) HCBS for disabled/elderly',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'New Mexico Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Mi Via Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written and skills competency evaluation, be at least 18 years old, have high school diploma or GED (required by most employers), pass background check before employment/certification, and undergo annual performance review by agency',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.hsd.state.nm.us/mi-via/',
                'phone': '(505) 827-3100',
                'email': 'mi.via@state.nm.us'
            },
            {
                'state': new_mexico,
                'program_name': 'Developmental Disabilities (DD) Waiver',
                'administering_agency': 'New Mexico Department of Health (DOH), Division of Health Improvement',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'New Mexico Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for DD Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written and skills competency evaluation, be at least 18 years old, have high school diploma or GED (required by most employers), pass background check before employment/certification, and undergo annual performance review by agency',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.hsd.state.nm.us/dd-waiver/',
                'phone': '(505) 827-3100',
                'email': 'dd.waiver@state.nm.us'
            },
            {
                'state': new_mexico,
                'program_name': 'Medically Fragile Waiver',
                'administering_agency': 'New Mexico Department of Health (DOH), Division of Health Improvement',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'New Mexico Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medically Fragile Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass written and skills competency evaluation, be at least 18 years old, have high school diploma or GED (required by most employers), pass background check before employment/certification, and undergo annual performance review by agency',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.hsd.state.nm.us/medically-fragile-waiver/',
                'phone': '(505) 827-3100',
                'email': 'medically.fragile@state.nm.us'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated New Mexico waiver programs')) 