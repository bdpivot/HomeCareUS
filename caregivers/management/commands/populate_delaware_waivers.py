from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Delaware waiver programs'

    def handle(self, *args, **kwargs):
        delaware = State.objects.get(abbreviation='DE')
        
        waiver_programs = [
            {
                'state': delaware,
                'program_name': 'Diamond State Health Plan-Plus (DSHP-Plus)',
                'administering_agency': 'Delaware Department of Health and Social Services (DHSS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI. All HCBS 1915(c) waivers (except DDDS Lifespan) consolidated into this program',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Delaware Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for DSHP-Plus, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training, pass Delaware HHA competency exam, pass background check, pass drug test, and complete 2-step PPD test',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'DHSS Training Portal, State-approved HHA training programs',
                'website': 'https://dhss.delaware.gov/dhss/dhcq/ohflcmain.html',
                'phone': '(302) 255-9040',
                'email': 'dhss.dhcq@delaware.gov'
            },
            {
                'state': delaware,
                'program_name': 'Delaware Medicaid State Plan',
                'administering_agency': 'Delaware Department of Health and Social Services (DHSS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Delaware Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid State Plan, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of state-approved HHA training, pass Delaware HHA competency exam, pass background check, pass drug test, and complete 2-step PPD test',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'DHSS Training Portal, State-approved HHA training programs',
                'website': 'https://dhss.delaware.gov/dhss/dhcq/ohflcmain.html',
                'phone': '(302) 255-9040',
                'email': 'dhss.dhcq@delaware.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Delaware waiver programs')) 