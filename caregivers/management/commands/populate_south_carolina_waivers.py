from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates South Carolina waiver programs'

    def handle(self, *args, **kwargs):
        south_carolina = State.objects.get(abbreviation='SC')
        
        waiver_programs = [
            {
                'state': south_carolina,
                'program_name': 'Community Long Term Care (CLTC) Waiver Programs',
                'administering_agency': 'South Carolina Department of Health and Human Services (SCDHHS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and other supports',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam (written and skills evaluation); must be at least 18 years old; must be literate and able to communicate effectively; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; home health agencies must offer skilled nursing and may offer other skilled services; in-home care providers and home health agencies are regulated separately',
                'annual_training_requirements': 'Continuing education required to maintain certification; renew certification periodically per DHEC requirements',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency maintains internal records of HHA qualifications and training',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CLTC Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam; must be at least 18 years old; must be literate and able to communicate effectively; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'http://www.scdhhs.gov/resources/waiver-managementfield-management',
                'phone': '(803) 898-2504',
                'email': 'waiver@scdhhs.gov'
            },
            {
                'state': south_carolina,
                'program_name': 'Head and Spinal Cord Injury (HASCI) Waiver',
                'administering_agency': 'South Carolina Department of Health and Human Services (SCDHHS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and other supports',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam (written and skills evaluation); must be at least 18 years old; must be literate and able to communicate effectively; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; home health agencies must offer skilled nursing and may offer other skilled services; in-home care providers and home health agencies are regulated separately',
                'annual_training_requirements': 'Continuing education required to maintain certification; renew certification periodically per DHEC requirements',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency maintains internal records of HHA qualifications and training',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HASCI Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam; must be at least 18 years old; must be literate and able to communicate effectively; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'http://www.scdhhs.gov/resources/waiver-managementfield-management',
                'phone': '(803) 898-2504',
                'email': 'hasci@scdhhs.gov'
            },
            {
                'state': south_carolina,
                'program_name': 'Intellectual Disability/Related Disabilities (ID/RD) Waiver',
                'administering_agency': 'South Carolina Department of Health and Human Services (SCDHHS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and other supports',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam (written and skills evaluation); must be at least 18 years old; must be literate and able to communicate effectively; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; home health agencies must offer skilled nursing and may offer other skilled services; in-home care providers and home health agencies are regulated separately',
                'annual_training_requirements': 'Continuing education required to maintain certification; renew certification periodically per DHEC requirements',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency maintains internal records of HHA qualifications and training',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for ID/RD Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam; must be at least 18 years old; must be literate and able to communicate effectively; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'http://www.scdhhs.gov/resources/waiver-managementfield-management',
                'phone': '(803) 898-2504',
                'email': 'idrd@scdhhs.gov'
            },
            {
                'state': south_carolina,
                'program_name': 'Community Supports (CS) Waiver',
                'administering_agency': 'South Carolina Department of Health and Human Services (SCDHHS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and other supports',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam (written and skills evaluation); must be at least 18 years old; must be literate and able to communicate effectively; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; home health agencies must offer skilled nursing and may offer other skilled services; in-home care providers and home health agencies are regulated separately',
                'annual_training_requirements': 'Continuing education required to maintain certification; renew certification periodically per DHEC requirements',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency maintains internal records of HHA qualifications and training',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam; must be at least 18 years old; must be literate and able to communicate effectively; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'http://www.scdhhs.gov/resources/waiver-managementfield-management',
                'phone': '(803) 898-2504',
                'email': 'cs@scdhhs.gov'
            },
            {
                'state': south_carolina,
                'program_name': 'Palmetto Coordinated System of Care (PCSC) Waiver',
                'administering_agency': 'South Carolina Department of Health and Human Services (SCDHHS)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and other supports',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam (written and skills evaluation); must be at least 18 years old; must be literate and able to communicate effectively; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; home health agencies must offer skilled nursing and may offer other skilled services; in-home care providers and home health agencies are regulated separately',
                'annual_training_requirements': 'Continuing education required to maintain certification; renew certification periodically per DHEC requirements',
                'effective_date': '2024-01-01',
                'registry_name': 'Agency maintains internal records of HHA qualifications and training',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for PCSC Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass South Carolina HHA certification exam; must be at least 18 years old; must be literate and able to communicate effectively; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'http://www.scdhhs.gov/resources/waiver-managementfield-management',
                'phone': '(803) 898-2504',
                'email': 'pcsc@scdhhs.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated South Carolina waiver programs')) 