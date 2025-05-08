from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Idaho waiver programs'

    def handle(self, *args, **kwargs):
        idaho = State.objects.get(abbreviation='ID')
        
        waiver_programs = [
            {
                'state': idaho,
                'program_name': 'Idaho Medicaid Home Health Services',
                'administering_agency': 'Idaho Department of Health and Welfare, Bureau of Facility Standards',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '24 hours continuing education every two years required',
                'effective_date': '2024-01-01',
                'registry_name': 'Idaho Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA, complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'Idaho State University, North Idaho College, State-approved HHA training programs',
                'website': 'https://healthandwelfare.idaho.gov/providers/acute-and-continuing-care/home-health-agencies',
                'phone': '(208) 334-6626',
                'email': 'bureau.facilitystandards@dhw.idaho.gov'
            },
            {
                'state': idaho,
                'program_name': 'Aged and Disabled (A&D) Waiver',
                'administering_agency': 'Idaho Department of Health and Welfare, Bureau of Facility Standards',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be elderly or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '24 hours continuing education every two years required',
                'effective_date': '2024-01-01',
                'registry_name': 'Idaho Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for A&D Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA, complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'Idaho State University, North Idaho College, State-approved HHA training programs',
                'website': 'https://healthandwelfare.idaho.gov/providers/home-and-community-based-long-term-care/long-term-care-provider-training',
                'phone': '(208) 334-6626',
                'email': 'bureau.facilitystandards@dhw.idaho.gov'
            },
            {
                'state': idaho,
                'program_name': 'Developmental Disabilities (DD) Waiver',
                'administering_agency': 'Idaho Department of Health and Welfare, Bureau of Facility Standards',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must have developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '24 hours continuing education every two years required',
                'effective_date': '2024-01-01',
                'registry_name': 'Idaho Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for DD Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA, complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'Idaho State University, North Idaho College, State-approved HHA training programs',
                'website': 'https://healthandwelfare.idaho.gov/providers/home-and-community-based-long-term-care/long-term-care-provider-training',
                'phone': '(208) 334-6626',
                'email': 'bureau.facilitystandards@dhw.idaho.gov'
            },
            {
                'state': idaho,
                'program_name': 'Children\'s Developmental Disabilities Waiver',
                'administering_agency': 'Idaho Department of Health and Welfare, Bureau of Facility Standards',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be child with developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '24 hours continuing education every two years required',
                'effective_date': '2024-01-01',
                'registry_name': 'Idaho Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Children\'s DD Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA, complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'Idaho State University, North Idaho College, State-approved HHA training programs',
                'website': 'https://healthandwelfare.idaho.gov/providers/home-and-community-based-long-term-care/long-term-care-provider-training',
                'phone': '(208) 334-6626',
                'email': 'bureau.facilitystandards@dhw.idaho.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Idaho waiver programs')) 