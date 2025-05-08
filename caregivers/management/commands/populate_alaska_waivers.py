from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Alaska waiver programs'

    def handle(self, *args, **kwargs):
        alaska = State.objects.get(abbreviation='AK')
        
        waiver_programs = [
            {
                'state': alaska,
                'program_name': 'Personal Care Services (PCS) Program',
                'administering_agency': 'Alaska Department of Health and Social Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day services, home modifications, specialized medical equipment',
                'unique_requirements': 'Must meet nursing facility level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours of continuing education required annually',
                'effective_date': '2024-01-01',
                'registry_name': 'Alaska Nurse Aide Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for Waiver Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be CNA certified, complete 140 hours training (80 clinical), pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'Alaska DHSS Training Portal, Alaska Training Cooperative',
                'website': 'https://health.alaska.gov/dhcs/Pages/waivers/default.aspx',
                'phone': '(907) 465-3030',
                'email': 'dhss.waiver@alaska.gov'
            },
            {
                'state': alaska,
                'program_name': 'Consumer Directed Personal Care Services (CDPCS)',
                'administering_agency': 'Alaska Department of Health and Social Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day services, home modifications, specialized medical equipment',
                'unique_requirements': 'Must meet nursing facility level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours of continuing education required annually',
                'effective_date': '2024-01-01',
                'registry_name': 'Alaska Nurse Aide Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for Waiver Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be CNA certified, complete 140 hours training (80 clinical), pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': False,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'Alaska DHSS Training Portal, Alaska Training Cooperative',
                'website': 'https://health.alaska.gov/dhcs/Pages/waivers/default.aspx',
                'phone': '(907) 465-3030',
                'email': 'dhss.waiver@alaska.gov'
            },
            {
                'state': alaska,
                'program_name': 'Alaskans Living Independently Medicaid Waiver',
                'administering_agency': 'Alaska Department of Health and Social Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day services, home-delivered meals, home modifications, emergency response system',
                'unique_requirements': 'Must meet assisted living level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours of continuing education required annually',
                'effective_date': '2024-01-01',
                'registry_name': 'Alaska Nurse Aide Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for Waiver Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be CNA certified, complete 140 hours training (80 clinical), pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'Alaska DHSS Training Portal, Alaska Training Cooperative',
                'website': 'https://health.alaska.gov/dhcs/Pages/waivers/default.aspx',
                'phone': '(907) 465-3030',
                'email': 'dhss.waiver@alaska.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Alaska waiver programs')) 