from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Iowa waiver programs'

    def handle(self, *args, **kwargs):
        iowa = State.objects.get(abbreviation='IA')
        
        waiver_programs = [
            {
                'state': iowa,
                'program_name': 'Iowa Medicaid Home Health Services',
                'administering_agency': 'Iowa Department of Inspections and Appeals (DIA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Iowa Direct Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16-30 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, have CPR/First Aid certification, and have Mandatory Abuse Reporting certification',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'DIA Training Portal, State-approved HHA training programs',
                'website': 'https://hhs.iowa.gov/programs/welcome-iowa-medicaid/iowa-medicaid-programs/home-health',
                'phone': '(515) 281-4115',
                'email': 'dia.health@dia.iowa.gov'
            },
            {
                'state': iowa,
                'program_name': 'IA Health Link',
                'administering_agency': 'Iowa Department of Inspections and Appeals (DIA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Iowa Direct Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for IA Health Link, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16-30 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, have CPR/First Aid certification, and have Mandatory Abuse Reporting certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'DIA Training Portal, State-approved HHA training programs',
                'website': 'https://hhs.iowa.gov/programs/welcome-iowa-medicaid/iowa-medicaid-programs/ia-health-link',
                'phone': '(515) 281-4115',
                'email': 'dia.health@dia.iowa.gov'
            },
            {
                'state': iowa,
                'program_name': 'Elderly Waiver',
                'administering_agency': 'Iowa Department of Inspections and Appeals (DIA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be elderly, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Iowa Direct Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Elderly Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16-30 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, have CPR/First Aid certification, and have Mandatory Abuse Reporting certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'DIA Training Portal, State-approved HHA training programs',
                'website': 'https://www.iowalegalaid.org/resource/elderly-waiver-program-keeps-people-out-of-nursing-homes',
                'phone': '(515) 281-4115',
                'email': 'dia.health@dia.iowa.gov'
            },
            {
                'state': iowa,
                'program_name': 'Health and Disability Waiver',
                'administering_agency': 'Iowa Department of Inspections and Appeals (DIA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Iowa Direct Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Health and Disability Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16-30 clinical hours) of state-approved HHA training, pass competency exam, pass background check, have high school diploma or GED, be 18 years old, have CPR/First Aid certification, and have Mandatory Abuse Reporting certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'DIA Training Portal, State-approved HHA training programs',
                'website': 'https://hhs.iowa.gov/programs/welcome-iowa-medicaid/iowa-medicaid-programs/home-health',
                'phone': '(515) 281-4115',
                'email': 'dia.health@dia.iowa.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Iowa waiver programs')) 