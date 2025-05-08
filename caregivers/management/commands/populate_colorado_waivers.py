from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Colorado waiver programs'

    def handle(self, *args, **kwargs):
        colorado = State.objects.get(abbreviation='CO')
        
        waiver_programs = [
            {
                'state': colorado,
                'program_name': 'Health First Colorado (Medicaid) – Home Health Program',
                'administering_agency': 'Colorado Department of Health Care Policy & Financing (HCPF)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Colorado Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Health First Colorado, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'Agency-based training programs, SNAP recipient programs',
                'website': 'https://hcpf.colorado.gov/home-health-program-0',
                'phone': '(303) 866-2993',
                'email': 'hcpf.homehealth@state.co.us'
            },
            {
                'state': colorado,
                'program_name': 'Long-Term Home Health (LTHH) Services',
                'administering_agency': 'Colorado Department of Health Care Policy & Financing (HCPF)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care, have income below 300% of SSI, and receive prior authorization from Options for Long Term Care agency',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Colorado Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for LTHH, Level of Care Assessment, Financial Assessment, Prior Authorization Form',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'Agency-based training programs, SNAP recipient programs',
                'website': 'https://hcpf.colorado.gov/home-health-faq',
                'phone': '(303) 866-2993',
                'email': 'hcpf.lthh@state.co.us'
            },
            {
                'state': colorado,
                'program_name': 'Acute Home Health Services',
                'administering_agency': 'Colorado Department of Health Care Policy & Financing (HCPF)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI. Care plan reviewed every 60 days',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Colorado Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Acute Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'Agency-based training programs, SNAP recipient programs',
                'website': 'https://hcpf.colorado.gov/home-health-program-0',
                'phone': '(303) 866-2993',
                'email': 'hcpf.acute@state.co.us'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Colorado waiver programs')) 