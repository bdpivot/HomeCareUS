from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates New York waiver programs'

    def handle(self, *args, **kwargs):
        new_york = State.objects.get(abbreviation='NY')
        
        waiver_programs = [
            {
                'state': new_york,
                'program_name': 'New York Medicaid Home Health Services',
                'administering_agency': 'New York State Department of Health (NYSDOH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed home care agency for Medicaid/Medicare reimbursement',
                'annual_training_requirements': 'Continuing education required for recertification (every 3 years)',
                'effective_date': '2024-01-01',
                'registry_name': 'New York State Home Care Worker Registry (HCWR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment, Up-to-date physical exam',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75+ total hours of state-approved Home Health Aide Training Program (HHATP) or equivalent, complete classroom and clinical training (e.g., 76 classroom hours + 1 day clinical at some programs), pass competency evaluation program (if not full HHATP), receive certificate of completion issued by approved program, be listed on the Home Care Worker Registry, have up-to-date physical exam, have high school diploma or equivalent (recommended by many employers), and pass criminal background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; additional training may be required by employer (infection control, dementia care, etc.)',
                'website': 'https://www.health.ny.gov/facilities/home_care/',
                'phone': '(518) 402-0996',
                'email': 'homecare@health.ny.gov'
            },
            {
                'state': new_york,
                'program_name': 'Managed Long-Term Care (MLTC) Program',
                'administering_agency': 'New York State Department of Health (NYSDOH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Continuing education required for recertification (every 3 years)',
                'effective_date': '2024-01-01',
                'registry_name': 'New York State Home Care Worker Registry (HCWR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MLTC Program, Level of Care Assessment, Financial Assessment, Up-to-date physical exam',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75+ total hours of state-approved Home Health Aide Training Program (HHATP) or equivalent, complete classroom and clinical training (e.g., 76 classroom hours + 1 day clinical at some programs), pass competency evaluation program (if not full HHATP), receive certificate of completion issued by approved program, be listed on the Home Care Worker Registry, have up-to-date physical exam, have high school diploma or equivalent (recommended by many employers), and pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.50,
                'salary_range_max': 22.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; additional training may be required by employer (infection control, dementia care, etc.)',
                'website': 'https://www.health.ny.gov/health_care/medicaid/program/longterm/mltc.htm',
                'phone': '(518) 402-0996',
                'email': 'mltc@health.ny.gov'
            },
            {
                'state': new_york,
                'program_name': 'Nursing Home Transition and Diversion (NHTD) Waiver',
                'administering_agency': 'New York State Department of Health (NYSDOH)',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Continuing education required for recertification (every 3 years)',
                'effective_date': '2024-01-01',
                'registry_name': 'New York State Home Care Worker Registry (HCWR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for NHTD Waiver, Level of Care Assessment, Financial Assessment, Up-to-date physical exam',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75+ total hours of state-approved Home Health Aide Training Program (HHATP) or equivalent, complete classroom and clinical training (e.g., 76 classroom hours + 1 day clinical at some programs), pass competency evaluation program (if not full HHATP), receive certificate of completion issued by approved program, be listed on the Home Care Worker Registry, have up-to-date physical exam, have high school diploma or equivalent (recommended by many employers), and pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 18.00,
                'salary_range_max': 23.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; additional training may be required by employer (infection control, dementia care, etc.)',
                'website': 'https://www.health.ny.gov/facilities/long_term_care/nhtd/',
                'phone': '(518) 402-0996',
                'email': 'nhtd@health.ny.gov'
            },
            {
                'state': new_york,
                'program_name': 'Traumatic Brain Injury (TBI) Waiver',
                'administering_agency': 'New York State Department of Health (NYSDOH)',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': 'Continuing education required for recertification (every 3 years)',
                'effective_date': '2024-01-01',
                'registry_name': 'New York State Home Care Worker Registry (HCWR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for TBI Waiver, Level of Care Assessment, Financial Assessment, Up-to-date physical exam',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75+ total hours of state-approved Home Health Aide Training Program (HHATP) or equivalent, complete classroom and clinical training (e.g., 76 classroom hours + 1 day clinical at some programs), pass competency evaluation program (if not full HHATP), receive certificate of completion issued by approved program, be listed on the Home Care Worker Registry, have up-to-date physical exam, have high school diploma or equivalent (recommended by many employers), and pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 18.50,
                'salary_range_max': 23.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; additional training may be required by employer (infection control, dementia care, etc.)',
                'website': 'https://www.health.ny.gov/facilities/long_term_care/tbi/',
                'phone': '(518) 402-0996',
                'email': 'tbi@health.ny.gov'
            },
            {
                'state': new_york,
                'program_name': 'Consumer Directed Personal Assistance Program (CDPAP)',
                'administering_agency': 'New York State Department of Health (NYSDOH)',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; all aides must register with the Public Partnerships, LLC (PPL) fiscal intermediary by March 28, 2025; temporary restraining order on some CDPAP changes-participants should continue registering and take a 4-hour certification course if needed',
                'annual_training_requirements': 'Continuing education required for recertification (every 3 years)',
                'effective_date': '2024-01-01',
                'registry_name': 'New York State Home Care Worker Registry (HCWR)',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CDPAP, Level of Care Assessment, Financial Assessment, Up-to-date physical exam',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75+ total hours of state-approved Home Health Aide Training Program (HHATP) or equivalent, complete classroom and clinical training (e.g., 76 classroom hours + 1 day clinical at some programs), pass competency evaluation program (if not full HHATP), receive certificate of completion issued by approved program, be listed on the Home Care Worker Registry, have up-to-date physical exam, have high school diploma or equivalent (recommended by many employers), and pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 19.00,
                'salary_range_max': 24.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available; additional training may be required by employer (infection control, dementia care, etc.)',
                'website': 'https://www.health.ny.gov/health_care/medicaid/program/longterm/cdpap/',
                'phone': '(518) 402-0996',
                'email': 'cdpap@health.ny.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated New York waiver programs')) 