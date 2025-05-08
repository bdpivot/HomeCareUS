from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Alabama waiver programs'

    def handle(self, *args, **kwargs):
        alabama = State.objects.get(abbreviation='AL')
        
        waiver_programs = [
            {
                'state': alabama,
                'program_name': 'Elderly and Disabled Waiver',
                'administering_agency': 'Alabama Medicaid Agency',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be 65 or older or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '8 hours of continuing education required annually',
                'effective_date': '2024-01-01',
                'registry_name': 'Alabama Medicaid Provider Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for Waiver Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete basic training and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 10.00,
                'salary_range_max': 15.00,
                'free_training_available': True,
                'free_training_programs': 'Alabama Medicaid Training Portal, Alabama Department of Senior Services Training',
                'website': 'https://medicaid.alabama.gov/content/4.0_Programs/4.4_Elderly_and_Disabled.aspx',
                'phone': '(800) 362-1504',
                'email': 'medicaid.waiver@medicaid.alabama.gov'
            },
            {
                'state': alabama,
                'program_name': 'Intellectual Disabilities Waiver',
                'administering_agency': 'Alabama Department of Mental Health',
                'services_offered': 'Personal care, habilitation, respite care, supported employment, day habilitation, home modifications, specialized medical equipment',
                'unique_requirements': 'Must have intellectual disability, meet ICF/IID level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours of continuing education required annually',
                'effective_date': '2024-01-01',
                'registry_name': 'Alabama Provider Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for Waiver Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete specialized training and pass enhanced background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'Alabama Department of Mental Health Training Portal, Alabama Council on Developmental Disabilities Training',
                'website': 'https://mh.alabama.gov/divisions/developmental-disabilities/',
                'phone': '(800) 367-0955',
                'email': 'idd.waiver@mh.alabama.gov'
            },
            {
                'state': alabama,
                'program_name': 'Living at Home Waiver',
                'administering_agency': 'Alabama Department of Senior Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, emergency response system',
                'unique_requirements': 'Must be 65 or older, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '6 hours of continuing education required annually',
                'effective_date': '2024-01-01',
                'registry_name': 'Alabama Senior Services Provider Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for Waiver Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete basic training and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 9.50,
                'salary_range_max': 14.50,
                'free_training_available': True,
                'free_training_programs': 'Alabama Department of Senior Services Training Portal, Alabama Aging Network Training',
                'website': 'https://www.alabamaageline.gov/',
                'phone': '(800) 243-5463',
                'email': 'senior.services@adss.alabama.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Alabama waiver programs')) 