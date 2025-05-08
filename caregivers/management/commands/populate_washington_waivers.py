from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Washington waiver programs'

    def handle(self, *args, **kwargs):
        washington = State.objects.get(abbreviation='WA')
        
        waiver_programs = [
            {
                'state': washington,
                'program_name': 'Washington Apple Health (Medicaid) Home Health Services',
                'administering_agency': 'Washington State Department of Health (DOH)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and home modifications',
                'unique_requirements': 'Must complete 85 total hours (35 hours core basic, 50 hours population-specific including 5 clinical); must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'annual_training_requirements': '12 hours annual continuing education to maintain certification; must work at least 8 hours every year to remain active',
                'effective_date': '2024-01-01',
                'registry_name': 'Washington State Department of Health Home Care Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Apple Health Home Health Services, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 85 total hours of training; must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.doh.wa.gov/LicensesPermitsandCertificates/HomeCareAide',
                'phone': '(360) 236-4700',
                'email': 'hca@doh.wa.gov'
            },
            {
                'state': washington,
                'program_name': 'Community Options Program Entry System (COPES) Waiver',
                'administering_agency': 'Department of Social and Health Services (DSHS), Aging and Long-Term Support Administration (ALTSA)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and home modifications',
                'unique_requirements': 'Must complete 85 total hours (35 hours core basic, 50 hours population-specific including 5 clinical); must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'annual_training_requirements': '12 hours annual continuing education to maintain certification; must work at least 8 hours every year to remain active',
                'effective_date': '2024-01-01',
                'registry_name': 'Washington State Department of Health Home Care Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for COPES Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 85 total hours of training; must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.50,
                'salary_range_max': 22.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dshs.wa.gov/altsa/home-and-community-services/copes',
                'phone': '(800) 422-3263',
                'email': 'altsa.info@dshs.wa.gov'
            },
            {
                'state': washington,
                'program_name': 'Medicaid Personal Care (MPC) Program',
                'administering_agency': 'Department of Social and Health Services (DSHS), Aging and Long-Term Support Administration (ALTSA)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and home modifications',
                'unique_requirements': 'Must complete 85 total hours (35 hours core basic, 50 hours population-specific including 5 clinical); must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'annual_training_requirements': '12 hours annual continuing education to maintain certification; must work at least 8 hours every year to remain active',
                'effective_date': '2024-01-01',
                'registry_name': 'Washington State Department of Health Home Care Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MPC Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 85 total hours of training; must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dshs.wa.gov/altsa/home-and-community-services/medicaid-personal-care',
                'phone': '(800) 422-3263',
                'email': 'altsa.info@dshs.wa.gov'
            },
            {
                'state': washington,
                'program_name': 'New Freedom Waiver',
                'administering_agency': 'Department of Social and Health Services (DSHS), Aging and Long-Term Support Administration (ALTSA)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and home modifications',
                'unique_requirements': 'Must complete 85 total hours (35 hours core basic, 50 hours population-specific including 5 clinical); must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'annual_training_requirements': '12 hours annual continuing education to maintain certification; must work at least 8 hours every year to remain active',
                'effective_date': '2024-01-01',
                'registry_name': 'Washington State Department of Health Home Care Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for New Freedom Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 85 total hours of training; must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dshs.wa.gov/altsa/home-and-community-services/new-freedom',
                'phone': '(800) 422-3263',
                'email': 'altsa.info@dshs.wa.gov'
            },
            {
                'state': washington,
                'program_name': 'Residential Support Waiver',
                'administering_agency': 'Department of Social and Health Services (DSHS), Aging and Long-Term Support Administration (ALTSA)',
                'services_offered': 'Personal care, respite, homemaker, skilled nursing, and home modifications',
                'unique_requirements': 'Must complete 85 total hours (35 hours core basic, 50 hours population-specific including 5 clinical); must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'annual_training_requirements': '12 hours annual continuing education to maintain certification; must work at least 8 hours every year to remain active',
                'effective_date': '2024-01-01',
                'registry_name': 'Washington State Department of Health Home Care Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Residential Support Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 85 total hours of training; must pass written and skills certification exam; must complete state-approved Home Care Aide training program; must apply for Home Care Aide certification within 14 days of hire; must be at least 18 years old; must have high school diploma or GED; must pass background check and fingerprinting; must have CPR/First Aid certification',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dshs.wa.gov/altsa/home-and-community-services/residential-support',
                'phone': '(800) 422-3263',
                'email': 'altsa.info@dshs.wa.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Washington waiver programs')) 