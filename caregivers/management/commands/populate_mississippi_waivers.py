from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Mississippi waiver programs'

    def handle(self, *args, **kwargs):
        mississippi = State.objects.get(abbreviation='MS')
        
        waiver_programs = [
            {
                'state': mississippi,
                'program_name': 'Mississippi Medicaid Home Health Services',
                'administering_agency': 'Mississippi Department of Health (MSDH), Division of Health Facilities Licensure and Certification',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Mississippi Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass Mississippi HHA certification test (written and skills), have high school diploma or GED, be at least 18 years old, pass background check, health exam, and drug screening, and be listed on Mississippi Nurse Aide Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 10.00,
                'salary_range_max': 15.00,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients and through some agencies',
                'website': 'https://msdh.ms.gov/page/30,0,82.html',
                'phone': '(601) 576-7400',
                'email': 'healthfacilities@msdh.ms.gov'
            },
            {
                'state': mississippi,
                'program_name': 'Elderly and Disabled Waiver',
                'administering_agency': 'Mississippi Division of Medicaid',
                'services_offered': 'Personal care, respite care, homemaker services',
                'unique_requirements': 'Must be senior or adult with disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Mississippi Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Elderly and Disabled Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass Mississippi HHA certification test (written and skills), have high school diploma or GED, be at least 18 years old, pass background check, health exam, and drug screening, and be listed on Mississippi Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 10.50,
                'salary_range_max': 15.50,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients and through some agencies',
                'website': 'https://medicaid.ms.gov/',
                'phone': '(601) 359-6050',
                'email': 'medicaid@medicaid.ms.gov'
            },
            {
                'state': mississippi,
                'program_name': 'Independent Living Waiver',
                'administering_agency': 'Mississippi Division of Medicaid',
                'services_offered': 'Personal care, respite care, homemaker services',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Mississippi Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Independent Living Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training, pass Mississippi HHA certification test (written and skills), have high school diploma or GED, be at least 18 years old, pass background check, health exam, and drug screening, and be listed on Mississippi Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'Free HHA training available for SNAP recipients and through some agencies',
                'website': 'https://medicaid.ms.gov/',
                'phone': '(601) 359-6050',
                'email': 'medicaid@medicaid.ms.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Mississippi waiver programs')) 