from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Connecticut waiver programs'

    def handle(self, *args, **kwargs):
        connecticut = State.objects.get(abbreviation='CT')
        
        waiver_programs = [
            {
                'state': connecticut,
                'program_name': 'HUSKY Health (Connecticut Medicaid)',
                'administering_agency': 'Connecticut Department of Social Services (DSS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Connecticut Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HUSKY Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 hours Nurse Aide Training Program, pass Prometric CNA Competency Exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.00,
                'salary_range_max': 19.00,
                'free_training_available': True,
                'free_training_programs': 'DPH Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://portal.ct.gov/dss/health-and-home-care/connecticut-home-care-program-for-elders/connecticut-home-care-program-for-elders-chcpe',
                'phone': '(860) 424-4900',
                'email': 'dss.husky@ct.gov'
            },
            {
                'state': connecticut,
                'program_name': 'Connecticut Home Care Program for Elders (CHCPE)',
                'administering_agency': 'Connecticut Department of Social Services (DSS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be 65 or older, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Connecticut Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CHCPE, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 hours Nurse Aide Training Program, pass Prometric CNA Competency Exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'DPH Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://portal.ct.gov/dss/health-and-home-care/connecticut-home-care-program-for-elders/connecticut-home-care-program-for-elders-chcpe',
                'phone': '(860) 424-4900',
                'email': 'dss.chcpe@ct.gov'
            },
            {
                'state': connecticut,
                'program_name': 'Personal Care Attendant (PCA) Program',
                'administering_agency': 'Connecticut Department of Social Services (DSS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be disabled, meet nursing home level of care, and have income below 300% of SSI. Cannot hire spouse for Medicaid-funded PCA',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Connecticut Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for PCA Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 hours Nurse Aide Training Program, pass Prometric CNA Competency Exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'DPH Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://portal.ct.gov/dss/health-and-home-care/connecticut-home-care-program-for-elders/connecticut-home-care-program-for-elders-chcpe',
                'phone': '(860) 424-4900',
                'email': 'dss.pca@ct.gov'
            },
            {
                'state': connecticut,
                'program_name': 'Medicaid Waiver for Individual and Family Support',
                'administering_agency': 'Connecticut Department of Developmental Services (DDS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, Blended Supports, Customized Employment, Transitional Supports, Caregiver Training/Counseling',
                'unique_requirements': 'Must have developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Connecticut Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for DDS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 hours Nurse Aide Training Program, pass Prometric CNA Competency Exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'DPH Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://portal.ct.gov/dds/individuals-and-families/individual-and-family-support',
                'phone': '(860) 418-6000',
                'email': 'dds.waiver@ct.gov'
            },
            {
                'state': connecticut,
                'program_name': 'Medicaid Waiver for Employment and Day Supports',
                'administering_agency': 'Connecticut Department of Developmental Services (DDS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, Blended Supports, Customized Employment, Transitional Supports, Caregiver Training/Counseling',
                'unique_requirements': 'Must have developmental disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Connecticut Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for DDS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 hours Nurse Aide Training Program, pass Prometric CNA Competency Exam, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'DPH Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://portal.ct.gov/dds/individuals-and-families/employment-and-day-supports',
                'phone': '(860) 418-6000',
                'email': 'dds.waiver@ct.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Connecticut waiver programs')) 