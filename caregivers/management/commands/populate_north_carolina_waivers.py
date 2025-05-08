from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates North Carolina waiver programs'

    def handle(self, *args, **kwargs):
        north_carolina = State.objects.get(abbreviation='NC')
        
        waiver_programs = [
            {
                'state': north_carolina,
                'program_name': 'North Carolina Medicaid Home Health Services',
                'administering_agency': 'North Carolina Department of Health and Human Services (NCDHHS), Division of Health Service Regulation (DHSR), Acute and Home Care Licensure and Certification Section',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; each home care agency site must be separately licensed; license must be renewed annually; agencies may provide different levels of service: Level I (home management), Level II/III (personal care); no license required for agencies providing only Level I (home management) services',
                'annual_training_requirements': '12 hours annual continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'North Carolina Nurse Aide I Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training/competency evaluation program, pass written exam and demonstrate ability to perform essential tasks (minimum 70% score), have high school diploma or GED (required), be at least 18 years old (recommended by most employers), pass drug screening, and pass competency evaluation and annual performance review',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://info.ncdhhs.gov/dhsr/ahc/homecare.html',
                'phone': '(919) 855-3765',
                'email': 'homecare@dhhs.nc.gov'
            },
            {
                'state': north_carolina,
                'program_name': 'Community Alternatives Program for Disabled Adults (CAP/DA) Waiver',
                'administering_agency': 'North Carolina Department of Health and Human Services (NCDHHS), Division of Health Service Regulation (DHSR), Acute and Home Care Licensure and Certification Section',
                'services_offered': 'Personal care, respite, home modifications, and specialized supports',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; assessment required to determine waiver eligibility',
                'annual_training_requirements': '12 hours annual continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'North Carolina Nurse Aide I Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CAP/DA Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training/competency evaluation program, pass written exam and demonstrate ability to perform essential tasks (minimum 70% score), have high school diploma or GED (required), be at least 18 years old (recommended by most employers), pass drug screening, and pass competency evaluation and annual performance review',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://info.ncdhhs.gov/dhsr/ahc/capda.html',
                'phone': '(919) 855-3765',
                'email': 'capda@dhhs.nc.gov'
            },
            {
                'state': north_carolina,
                'program_name': 'Community Alternatives Program for Children (CAP/C) Waiver',
                'administering_agency': 'North Carolina Department of Health and Human Services (NCDHHS), Division of Health Service Regulation (DHSR), Acute and Home Care Licensure and Certification Section',
                'services_offered': 'Personal care, respite, home modifications, and specialized supports',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; assessment required to determine waiver eligibility',
                'annual_training_requirements': '12 hours annual continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'North Carolina Nurse Aide I Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CAP/C Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training/competency evaluation program, pass written exam and demonstrate ability to perform essential tasks (minimum 70% score), have high school diploma or GED (required), be at least 18 years old (recommended by most employers), pass drug screening, and pass competency evaluation and annual performance review',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://info.ncdhhs.gov/dhsr/ahc/capc.html',
                'phone': '(919) 855-3765',
                'email': 'capc@dhhs.nc.gov'
            },
            {
                'state': north_carolina,
                'program_name': 'Innovations Waiver',
                'administering_agency': 'North Carolina Department of Health and Human Services (NCDHHS), Division of Health Service Regulation (DHSR), Acute and Home Care Licensure and Certification Section',
                'services_offered': 'Personal care, respite, home modifications, and specialized supports',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; assessment required to determine waiver eligibility; for individuals with intellectual/developmental disabilities',
                'annual_training_requirements': '12 hours annual continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'North Carolina Nurse Aide I Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Innovations Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training/competency evaluation program, pass written exam and demonstrate ability to perform essential tasks (minimum 70% score), have high school diploma or GED (required), be at least 18 years old (recommended by most employers), pass drug screening, and pass competency evaluation and annual performance review',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://info.ncdhhs.gov/dhsr/ahc/innovations.html',
                'phone': '(919) 855-3765',
                'email': 'innovations@dhhs.nc.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated North Carolina waiver programs')) 