from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Oklahoma waiver programs'

    def handle(self, *args, **kwargs):
        oklahoma = State.objects.get(abbreviation='OK')
        
        waiver_programs = [
            {
                'state': oklahoma,
                'program_name': 'SoonerCare (Oklahoma Medicaid) Home Health Services',
                'administering_agency': 'Oklahoma State Department of Health (OSDH), Home Services Division',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed home care agency for Medicaid/Medicare reimbursement; home health aide visits are part-time/intermittent; home health services cannot be used for respite care; additional services (beyond limits) require prior authorization or recent hospitalization; all home health agencies must be licensed by OSDH; licenses valid for three years, renewable with continued compliance',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; 10 hours of Alzheimer\'s/dementia care training included in curriculum',
                'effective_date': '2024-01-01',
                'registry_name': 'Oklahoma Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for SoonerCare Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program, pass written and skills competency evaluation, have high school diploma or GED (recommended by most employers), be at least 18 years old (recommended by most employers), pass criminal background check (required before employment/certification), and pass fingerprinting (required for agency licensure and some employment)',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://oklahoma.gov/health/services/licensing-inspections/medical-facilities-service/home-services-division.html',
                'phone': '(405) 271-6868',
                'email': 'homeservices@health.ok.gov'
            },
            {
                'state': oklahoma,
                'program_name': 'ADvantage Waiver Program',
                'administering_agency': 'Oklahoma State Department of Health (OSDH), Home Services Division',
                'services_offered': 'Personal care, respite, homemaker, assisted living, home modifications, and adult day health',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; 1915(c) HCBS for elderly/disabled adults at risk of nursing home placement; waitlist may apply',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; 10 hours of Alzheimer\'s/dementia care training included in curriculum',
                'effective_date': '2024-01-01',
                'registry_name': 'Oklahoma Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for ADvantage Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program, pass written and skills competency evaluation, have high school diploma or GED (recommended by most employers), be at least 18 years old (recommended by most employers), pass criminal background check (required before employment/certification), and pass fingerprinting (required for agency licensure and some employment)',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://www.medicaidplanningassistance.org/oklahoma-advantage-waiver/',
                'phone': '(405) 271-6868',
                'email': 'advantage@health.ok.gov'
            },
            {
                'state': oklahoma,
                'program_name': 'Consumer Directed Personal Assistance Services and Supports (CD-PASS)',
                'administering_agency': 'Oklahoma State Department of Health (OSDH), Home Services Division',
                'services_offered': 'Personal care, respite, homemaker, and skilled nursing',
                'unique_requirements': 'Self-directed personal care under ADvantage Waiver; participant can hire, train, and manage caregiver, including family/friends, with background check and training; spouse can be hired only in rare cases',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification; 10 hours of Alzheimer\'s/dementia care training included in curriculum',
                'effective_date': '2024-01-01',
                'registry_name': 'Oklahoma Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CD-PASS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program, pass written and skills competency evaluation, have high school diploma or GED (recommended by most employers), be at least 18 years old (recommended by most employers), pass criminal background check (required before employment/certification), and pass fingerprinting (required for agency licensure and some employment)',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': False,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients; on-the-job training and approved programs available',
                'website': 'https://www.medicaidplanningassistance.org/oklahoma-advantage-waiver/',
                'phone': '(405) 271-6868',
                'email': 'cdpass@health.ok.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Oklahoma waiver programs')) 