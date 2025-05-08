from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates New Jersey waiver programs'

    def handle(self, *args, **kwargs):
        new_jersey = State.objects.get(abbreviation='NJ')
        
        waiver_programs = [
            {
                'state': new_jersey,
                'program_name': 'NJ FamilyCare (New Jersey Medicaid) Home Health Services',
                'administering_agency': 'New Jersey Board of Nursing, Division of Consumer Affairs',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed home health agency or health care service firm for Medicaid reimbursement',
                'annual_training_requirements': 'Renew certification every two years',
                'effective_date': '2024-01-01',
                'registry_name': 'New Jersey Board of Nursing Certified Homemaker-Home Health Aide (CHHA) Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment, 2×2 passport photo, government-issued ID, Social Security card, birth certificate or proof of eligibility to work in the US',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 76 total hours (60 classroom, 16 clinical) of state-approved CHHA training, pass written and skills competency exam, be at least 18 years old, be US citizen or eligible to work in the US, have high school diploma or equivalent (recommended), read, write, and speak English proficiently, have employment or promise of employment by an accredited home care agency before license can be issued, have mandatory attendance for full required hours, have clear criminal background and fingerprinting, and have physical capability for patient care tasks',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; special bridge course available for CNAs (10 hours); nursing students who have completed "Fundamentals of Nursing" may apply for CHHA without full 76-hour course',
                'website': 'https://www.nj.gov/humanservices/jobsthatcare/chha/about/',
                'phone': '(973) 504-6430',
                'email': 'chha@dca.njoag.gov'
            },
            {
                'state': new_jersey,
                'program_name': 'Community Choice Waiver',
                'administering_agency': 'New Jersey Department of Human Services, Division of Medical Assistance and Health Services (DMAHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Renew certification every two years',
                'effective_date': '2024-01-01',
                'registry_name': 'New Jersey Board of Nursing Certified Homemaker-Home Health Aide (CHHA) Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Community Choice Waiver, Level of Care Assessment, Financial Assessment, 2×2 passport photo, government-issued ID, Social Security card, birth certificate or proof of eligibility to work in the US',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 76 total hours (60 classroom, 16 clinical) of state-approved CHHA training, pass written and skills competency exam, be at least 18 years old, be US citizen or eligible to work in the US, have high school diploma or equivalent (recommended), read, write, and speak English proficiently, have employment or promise of employment by an accredited home care agency before license can be issued, have mandatory attendance for full required hours, have clear criminal background and fingerprinting, and have physical capability for patient care tasks',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; special bridge course available for CNAs (10 hours); nursing students who have completed "Fundamentals of Nursing" may apply for CHHA without full 76-hour course',
                'website': 'https://www.nj.gov/humanservices/dmahs/clients/communitychoice.html',
                'phone': '(609) 588-2600',
                'email': 'dmahs@dhs.nj.gov'
            },
            {
                'state': new_jersey,
                'program_name': 'Managed Long-Term Services and Supports (MLTSS) Waiver',
                'administering_agency': 'New Jersey Department of Human Services, Division of Medical Assistance and Health Services (DMAHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Renew certification every two years',
                'effective_date': '2024-01-01',
                'registry_name': 'New Jersey Board of Nursing Certified Homemaker-Home Health Aide (CHHA) Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MLTSS Waiver, Level of Care Assessment, Financial Assessment, 2×2 passport photo, government-issued ID, Social Security card, birth certificate or proof of eligibility to work in the US',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 76 total hours (60 classroom, 16 clinical) of state-approved CHHA training, pass written and skills competency exam, be at least 18 years old, be US citizen or eligible to work in the US, have high school diploma or equivalent (recommended), read, write, and speak English proficiently, have employment or promise of employment by an accredited home care agency before license can be issued, have mandatory attendance for full required hours, have clear criminal background and fingerprinting, and have physical capability for patient care tasks',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; special bridge course available for CNAs (10 hours); nursing students who have completed "Fundamentals of Nursing" may apply for CHHA without full 76-hour course',
                'website': 'https://www.nj.gov/humanservices/dmahs/clients/mltss.html',
                'phone': '(609) 588-2600',
                'email': 'dmahs@dhs.nj.gov'
            },
            {
                'state': new_jersey,
                'program_name': 'Personal Preference Program (PPP)',
                'administering_agency': 'New Jersey Department of Human Services, Division of Medical Assistance and Health Services (DMAHS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; proposed (A3564, 2024): Family members or approved individuals may become certified CHHAs and provide services under Medicaid/NJ FamilyCare for enrollees 65+',
                'annual_training_requirements': 'Renew certification every two years',
                'effective_date': '2024-01-01',
                'registry_name': 'New Jersey Board of Nursing Certified Homemaker-Home Health Aide (CHHA) Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for PPP, Level of Care Assessment, Financial Assessment, 2×2 passport photo, government-issued ID, Social Security card, birth certificate or proof of eligibility to work in the US',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 76 total hours (60 classroom, 16 clinical) of state-approved CHHA training, pass written and skills competency exam, be at least 18 years old, be US citizen or eligible to work in the US, have high school diploma or equivalent (recommended), read, write, and speak English proficiently, have employment or promise of employment by an accredited home care agency before license can be issued, have mandatory attendance for full required hours, have clear criminal background and fingerprinting, and have physical capability for patient care tasks',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.50,
                'salary_range_max': 22.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; special bridge course available for CNAs (10 hours); nursing students who have completed "Fundamentals of Nursing" may apply for CHHA without full 76-hour course',
                'website': 'https://www.nj.gov/humanservices/dmahs/clients/njppp.html',
                'phone': '(609) 588-2600',
                'email': 'dmahs@dhs.nj.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated New Jersey waiver programs')) 