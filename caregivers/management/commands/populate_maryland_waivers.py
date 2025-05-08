from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Maryland waiver programs'

    def handle(self, *args, **kwargs):
        maryland = State.objects.get(abbreviation='MD')
        
        waiver_programs = [
            {
                'state': maryland,
                'program_name': 'Maryland Medicaid Home Health Services',
                'administering_agency': 'Maryland Department of Health (MDH), Office of Health Care Quality',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maryland Board of Nursing CNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must be a CNA (100 classroom, 40 clinical hours), pass Maryland HHA competency exam, pass background check, have high school diploma or GED, and be listed on Maryland CNA Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'MDH Training Portal, State-approved HHA training programs',
                'website': 'https://health.maryland.gov/mbon/pages/cna-index.aspx',
                'phone': '(410) 585-1900',
                'email': 'mdh.info@maryland.gov'
            },
            {
                'state': maryland,
                'program_name': 'Community First Choice (CFC) Program',
                'administering_agency': 'Maryland Department of Health (MDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maryland Board of Nursing CNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CFC Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (100 classroom, 40 clinical hours), pass Maryland HHA competency exam, pass background check, have high school diploma or GED, and be listed on Maryland CNA Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.50,
                'salary_range_max': 18.50,
                'free_training_available': True,
                'free_training_programs': 'MDH Training Portal, State-approved HHA training programs',
                'website': 'https://health.maryland.gov/mbon/pages/cna-index.aspx',
                'phone': '(410) 585-1900',
                'email': 'mdh.info@maryland.gov'
            },
            {
                'state': maryland,
                'program_name': 'Home and Community-Based Options Waiver (CO Waiver)',
                'administering_agency': 'Maryland Department of Health (MDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maryland Board of Nursing CNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CO Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (100 classroom, 40 clinical hours), pass Maryland HHA competency exam, pass background check, have high school diploma or GED, and be listed on Maryland CNA Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'MDH Training Portal, State-approved HHA training programs',
                'website': 'https://health.maryland.gov/mbon/pages/cna-index.aspx',
                'phone': '(410) 585-1900',
                'email': 'mdh.info@maryland.gov'
            },
            {
                'state': maryland,
                'program_name': 'In-Home Aide Services (IHAS)',
                'administering_agency': 'Maryland Department of Health (MDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be at risk of nursing home placement, neglect, or without a caregiver; sliding scale fee based on income',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maryland Board of Nursing CNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for IHAS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (100 classroom, 40 clinical hours), pass Maryland HHA competency exam, pass background check, have high school diploma or GED, and be listed on Maryland CNA Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'MDH Training Portal, State-approved HHA training programs',
                'website': 'https://health.maryland.gov/mbon/pages/cna-index.aspx',
                'phone': '(410) 585-1900',
                'email': 'mdh.info@maryland.gov'
            },
            {
                'state': maryland,
                'program_name': 'Medical Day Care Services Waiver',
                'administering_agency': 'Maryland Department of Health (MDH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Maryland Board of Nursing CNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medical Day Care Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a CNA (100 classroom, 40 clinical hours), pass Maryland HHA competency exam, pass background check, have high school diploma or GED, and be listed on Maryland CNA Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'MDH Training Portal, State-approved HHA training programs',
                'website': 'https://health.maryland.gov/mbon/pages/cna-index.aspx',
                'phone': '(410) 585-1900',
                'email': 'mdh.info@maryland.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Maryland waiver programs')) 