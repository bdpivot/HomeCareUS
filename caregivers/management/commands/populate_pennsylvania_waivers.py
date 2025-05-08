from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Pennsylvania waiver programs'

    def handle(self, *args, **kwargs):
        pennsylvania = State.objects.get(abbreviation='PA')
        
        waiver_programs = [
            {
                'state': pennsylvania,
                'program_name': 'Medical Assistance (Pennsylvania Medicaid) Home Health Services',
                'administering_agency': 'Pennsylvania Department of Health (DOH), Division of Home Health',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED (required by law or completion of nurse aide program); competency may also be demonstrated by: valid nurse\'s license, nurse aide certification, or passing an employer-developed exam; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; agencies established after Dec 12, 2009 must obtain a license prior to providing services; provisional license may be issued if deficiencies are found, with a plan for correction',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; annual review of direct care worker competency required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medical Assistance Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must pass criminal background check and child abuse clearance (if applicable); must pass TB screening',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': '$500 HHA training grants available for new aides in 2025, with 16-hour classroom training and 40 hours work requirement; on-the-job training and approved programs available',
                'website': 'https://www.pa.gov/agencies/health/facilities/out-patient-healthcare-facilities/home-care/home-care-regulations.html',
                'phone': '(717) 783-1379',
                'email': 'ra-dhhomecare@pa.gov'
            },
            {
                'state': pennsylvania,
                'program_name': 'Living Independence for the Elderly (LIFE) Program',
                'administering_agency': 'Pennsylvania Department of Health (DOH), Division of Home Health',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; competency may also be demonstrated by: valid nurse\'s license, nurse aide certification, or passing an employer-developed exam',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; annual review of direct care worker competency required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for LIFE Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must pass criminal background check and child abuse clearance (if applicable); must pass TB screening',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': '$500 HHA training grants available for new aides in 2025, with 16-hour classroom training and 40 hours work requirement; on-the-job training and approved programs available',
                'website': 'https://www.pa.gov/agencies/health/facilities/out-patient-healthcare-facilities/home-care/home-care-regulations.html',
                'phone': '(717) 783-1379',
                'email': 'life@pa.gov'
            },
            {
                'state': pennsylvania,
                'program_name': 'Community HealthChoices (CHC) Waiver',
                'administering_agency': 'Pennsylvania Department of Health (DOH), Division of Home Health',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; competency may also be demonstrated by: valid nurse\'s license, nurse aide certification, or passing an employer-developed exam',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; annual review of direct care worker competency required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CHC Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must pass criminal background check and child abuse clearance (if applicable); must pass TB screening',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': '$500 HHA training grants available for new aides in 2025, with 16-hour classroom training and 40 hours work requirement; on-the-job training and approved programs available',
                'website': 'https://www.pa.gov/agencies/health/facilities/out-patient-healthcare-facilities/home-care/home-care-regulations.html',
                'phone': '(717) 783-1379',
                'email': 'chc@pa.gov'
            },
            {
                'state': pennsylvania,
                'program_name': 'Aging Waiver',
                'administering_agency': 'Pennsylvania Department of Health (DOH), Division of Home Health',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; competency may also be demonstrated by: valid nurse\'s license, nurse aide certification, or passing an employer-developed exam',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; annual review of direct care worker competency required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Aging Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must pass criminal background check and child abuse clearance (if applicable); must pass TB screening',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': '$500 HHA training grants available for new aides in 2025, with 16-hour classroom training and 40 hours work requirement; on-the-job training and approved programs available',
                'website': 'https://www.pa.gov/agencies/health/facilities/out-patient-healthcare-facilities/home-care/home-care-regulations.html',
                'phone': '(717) 783-1379',
                'email': 'aging@pa.gov'
            },
            {
                'state': pennsylvania,
                'program_name': 'Attendant Care/Act 150 Waiver',
                'administering_agency': 'Pennsylvania Department of Health (DOH), Division of Home Health',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; competency may also be demonstrated by: valid nurse\'s license, nurse aide certification, or passing an employer-developed exam',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; annual review of direct care worker competency required',
                'effective_date': '2024-01-01',
                'registry_name': 'Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Attendant Care/Act 150 Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must have high school diploma or GED; must pass criminal background check and child abuse clearance (if applicable); must pass TB screening',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': '$500 HHA training grants available for new aides in 2025, with 16-hour classroom training and 40 hours work requirement; on-the-job training and approved programs available',
                'website': 'https://www.pa.gov/agencies/health/facilities/out-patient-healthcare-facilities/home-care/home-care-regulations.html',
                'phone': '(717) 783-1379',
                'email': 'attendantcare@pa.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Pennsylvania waiver programs')) 