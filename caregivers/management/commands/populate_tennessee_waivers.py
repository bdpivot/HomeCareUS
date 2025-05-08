from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Tennessee waiver programs'

    def handle(self, *args, **kwargs):
        tennessee = State.objects.get(abbreviation='TN')
        
        waiver_programs = [
            {
                'state': tennessee,
                'program_name': 'TennCare (Tennessee Medicaid) Home Health Services',
                'administering_agency': 'Tennessee Department of Health, Division of Licensure and Regulation',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; training must be completed within three months of employment at a home health agency; proof of at least 8 hours worked each year required to remain active on Nurse Aide Registry; special exemptions for pediatric and EEOICPA-only agencies (no CON required, but must be accredited within two years)',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Tennessee Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for TennCare Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must pass criminal background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://www.tn.gov/hfc/division-of-licensure-and-regulation/nurse-aide-information.html',
                'phone': '(615) 741-7221',
                'email': 'health.licensure@tn.gov'
            },
            {
                'state': tennessee,
                'program_name': 'CHOICES in Long-Term Services and Supports (LTSS) Waiver',
                'administering_agency': 'Tennessee Department of Health, Division of Licensure and Regulation',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; training must be completed within three months of employment at a home health agency; proof of at least 8 hours worked each year required to remain active on Nurse Aide Registry; special exemptions for pediatric and EEOICPA-only agencies (no CON required, but must be accredited within two years)',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Tennessee Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CHOICES Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://www.tn.gov/hfc/division-of-licensure-and-regulation/nurse-aide-information.html',
                'phone': '(615) 741-7221',
                'email': 'choices@tn.gov'
            },
            {
                'state': tennessee,
                'program_name': 'Employment and Community First (ECF) CHOICES Waiver',
                'administering_agency': 'Tennessee Department of Health, Division of Licensure and Regulation',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; training must be completed within three months of employment at a home health agency; proof of at least 8 hours worked each year required to remain active on Nurse Aide Registry; special exemptions for pediatric and EEOICPA-only agencies (no CON required, but must be accredited within two years)',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Tennessee Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for ECF CHOICES Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://www.tn.gov/hfc/division-of-licensure-and-regulation/nurse-aide-information.html',
                'phone': '(615) 741-7221',
                'email': 'ecf@tn.gov'
            },
            {
                'state': tennessee,
                'program_name': 'Katie Beckett Waiver',
                'administering_agency': 'Tennessee Department of Health, Division of Licensure and Regulation',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be employed by a licensed home health agency for Medicaid/Medicare reimbursement; training must be completed within three months of employment at a home health agency; proof of at least 8 hours worked each year required to remain active on Nurse Aide Registry; special exemptions for pediatric and EEOICPA-only agencies (no CON required, but must be accredited within two years)',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Tennessee Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Katie Beckett Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://www.tn.gov/hfc/division-of-licensure-and-regulation/nurse-aide-information.html',
                'phone': '(615) 741-7221',
                'email': 'katiebeckett@tn.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Tennessee waiver programs')) 