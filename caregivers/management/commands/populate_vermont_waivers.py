from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Vermont waiver programs'

    def handle(self, *args, **kwargs):
        vermont = State.objects.get(abbreviation='VT')
        
        waiver_programs = [
            {
                'state': vermont,
                'program_name': 'Choices for Care (CFC) Waiver',
                'administering_agency': 'Vermont Department of Disabilities, Aging and Independent Living (DAIL)',
                'services_offered': 'Personal care, respite, homemaker, and enhanced residential care',
                'unique_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training (includes at least 16 clinical hours); must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact (safety, infection control, emergency procedures, communication, client rights); must apply for and maintain license with the Vermont Board of Nursing; must pass criminal background check; must meet documentation requirements as specified by Board of Nursing',
                'annual_training_requirements': 'Annual HHA training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency; continuing education may be required for license renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'Vermont Board of Nursing LNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Choices for Care Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training; must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dail.vermont.gov/regulations-designation-operation-hha',
                'phone': '(802) 241-2400',
                'email': 'dail.info@vermont.gov'
            },
            {
                'state': vermont,
                'program_name': 'Community First Choice (CFC) – Enhanced Waiver',
                'administering_agency': 'Vermont Department of Disabilities, Aging and Independent Living (DAIL)',
                'services_offered': 'Personal care, respite, homemaker, and enhanced residential care',
                'unique_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training (includes at least 16 clinical hours); must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact (safety, infection control, emergency procedures, communication, client rights); must apply for and maintain license with the Vermont Board of Nursing; must pass criminal background check; must meet documentation requirements as specified by Board of Nursing',
                'annual_training_requirements': 'Annual HHA training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency; continuing education may be required for license renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'Vermont Board of Nursing LNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Community First Choice Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training; must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dail.vermont.gov/regulations-designation-operation-hha',
                'phone': '(802) 241-2400',
                'email': 'dail.info@vermont.gov'
            },
            {
                'state': vermont,
                'program_name': 'Enhanced Residential Care (ERC) Waiver',
                'administering_agency': 'Vermont Department of Disabilities, Aging and Independent Living (DAIL)',
                'services_offered': 'Personal care, respite, homemaker, and enhanced residential care',
                'unique_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training (includes at least 16 clinical hours); must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact (safety, infection control, emergency procedures, communication, client rights); must apply for and maintain license with the Vermont Board of Nursing; must pass criminal background check; must meet documentation requirements as specified by Board of Nursing',
                'annual_training_requirements': 'Annual HHA training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency; continuing education may be required for license renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'Vermont Board of Nursing LNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Enhanced Residential Care Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training; must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.50,
                'salary_range_max': 22.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dail.vermont.gov/regulations-designation-operation-hha',
                'phone': '(802) 241-2400',
                'email': 'dail.info@vermont.gov'
            },
            {
                'state': vermont,
                'program_name': 'Family Caregiver Support (FCS) Waiver',
                'administering_agency': 'Vermont Department of Disabilities, Aging and Independent Living (DAIL)',
                'services_offered': 'Personal care, respite, homemaker, and enhanced residential care',
                'unique_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training (includes at least 16 clinical hours); must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact (safety, infection control, emergency procedures, communication, client rights); must apply for and maintain license with the Vermont Board of Nursing; must pass criminal background check; must meet documentation requirements as specified by Board of Nursing',
                'annual_training_requirements': 'Annual HHA training topics include infection control, communication skills, patient rights, and other topics as required by the employing agency; continuing education may be required for license renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'Vermont Board of Nursing LNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Family Caregiver Support Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 80 hours minimum for Licensed Nursing Assistant (LNA) training; must pass state-approved LNA training program; must pass certification exam; must have at least 16 hours of education before direct client contact; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 18.00,
                'salary_range_max': 23.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://dail.vermont.gov/regulations-designation-operation-hha',
                'phone': '(802) 241-2400',
                'email': 'dail.info@vermont.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Vermont waiver programs')) 