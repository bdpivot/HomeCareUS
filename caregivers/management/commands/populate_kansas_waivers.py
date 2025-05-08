from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Kansas waiver programs'

    def handle(self, *args, **kwargs):
        kansas = State.objects.get(abbreviation='KS')
        
        waiver_programs = [
            {
                'state': kansas,
                'program_name': 'KanCare (Kansas Medicaid Managed Care Program)',
                'administering_agency': 'Kansas Department of Health and Environment (KDHE)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kansas Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for KanCare, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (90 hours), complete 20 hours of HHA-specific training, pass HHA competency exam, pass background check, have high school diploma or GED, be 18 years old, and have valid driver\'s license',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'KDHE Training Portal, State-approved HHA training programs',
                'website': 'https://www.kancare.ks.gov/',
                'phone': '(785) 296-3981',
                'email': 'kancare@kdhe.ks.gov'
            },
            {
                'state': kansas,
                'program_name': 'Medicaid Home Health Services',
                'administering_agency': 'Kansas Department of Health and Environment (KDHE)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kansas Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must be a CNA (90 hours), complete 20 hours of HHA-specific training, pass HHA competency exam, pass background check, have high school diploma or GED, be 18 years old, and have valid driver\'s license',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'KDHE Training Portal, State-approved HHA training programs',
                'website': 'https://www.kdhe.ks.gov/',
                'phone': '(785) 296-3981',
                'email': 'kancare@kdhe.ks.gov'
            },
            {
                'state': kansas,
                'program_name': 'Frail Elderly HCBS Waiver',
                'administering_agency': 'Kansas Department for Aging and Disability Services (KDADS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be elderly, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kansas Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Frail Elderly Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (90 hours), complete 20 hours of HHA-specific training, pass HHA competency exam, pass background check, have high school diploma or GED, be 18 years old, and have valid driver\'s license',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'KDADS Training Portal, State-approved HHA training programs',
                'website': 'https://www.kdads.ks.gov/',
                'phone': '(785) 296-4986',
                'email': 'kdads.info@ks.gov'
            },
            {
                'state': kansas,
                'program_name': 'Physical Disability HCBS Waiver',
                'administering_agency': 'Kansas Department for Aging and Disability Services (KDADS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must have physical disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kansas Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Physical Disability Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (90 hours), complete 20 hours of HHA-specific training, pass HHA competency exam, pass background check, have high school diploma or GED, be 18 years old, and have valid driver\'s license',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'KDADS Training Portal, State-approved HHA training programs',
                'website': 'https://www.kdads.ks.gov/',
                'phone': '(785) 296-4986',
                'email': 'kdads.info@ks.gov'
            },
            {
                'state': kansas,
                'program_name': 'Intellectual/Developmental Disability (I/DD) HCBS Waiver',
                'administering_agency': 'Kansas Department for Aging and Disability Services (KDADS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must have intellectual/developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Kansas Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for I/DD Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (90 hours), complete 20 hours of HHA-specific training, pass HHA competency exam, pass background check, have high school diploma or GED, be 18 years old, and have valid driver\'s license',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'KDADS Training Portal, State-approved HHA training programs',
                'website': 'https://www.kdads.ks.gov/',
                'phone': '(785) 296-4986',
                'email': 'kdads.info@ks.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Kansas waiver programs')) 