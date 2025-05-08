from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates South Dakota waiver programs'

    def handle(self, *args, **kwargs):
        south_dakota = State.objects.get(abbreviation='SD')
        
        waiver_programs = [
            {
                'state': south_dakota,
                'program_name': 'South Dakota Medicaid Home Health Services',
                'administering_agency': 'South Dakota Department of Health (DOH), Office of Health Facilities Licensure and Certification',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must be listed on the South Dakota Nurse Aide Registry; must work as a nurse aide in a paid position within 24 months to stay active on the registry; reciprocity available for out-of-state nurse aides with equivalent training and recent employment',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'South Dakota Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must pass criminal background check and abuse/neglect registry check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://doh.sd.gov/boards/nursing/',
                'phone': '(605) 362-2760',
                'email': 'health.licensing@state.sd.us'
            },
            {
                'state': south_dakota,
                'program_name': 'Home and Community-Based Services (HCBS) Waiver',
                'administering_agency': 'South Dakota Department of Health (DOH), Office of Health Facilities Licensure and Certification',
                'services_offered': 'Personal care, respite, homemaker, and assisted living services',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must be listed on the South Dakota Nurse Aide Registry; must work as a nurse aide in a paid position within 24 months to stay active on the registry; reciprocity available for out-of-state nurse aides with equivalent training and recent employment',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'South Dakota Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must pass criminal background check and abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://doh.sd.gov/boards/nursing/',
                'phone': '(605) 362-2760',
                'email': 'hcbs@state.sd.us'
            },
            {
                'state': south_dakota,
                'program_name': 'Personal Care Services (PCS) Program',
                'administering_agency': 'South Dakota Department of Health (DOH), Office of Health Facilities Licensure and Certification',
                'services_offered': 'Personal care, respite, homemaker, and assisted living services',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must be listed on the South Dakota Nurse Aide Registry; must work as a nurse aide in a paid position within 24 months to stay active on the registry; reciprocity available for out-of-state nurse aides with equivalent training and recent employment',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'South Dakota Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for PCS Program, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must pass criminal background check and abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://doh.sd.gov/boards/nursing/',
                'phone': '(605) 362-2760',
                'email': 'pcs@state.sd.us'
            },
            {
                'state': south_dakota,
                'program_name': 'Assisted Living Waiver',
                'administering_agency': 'South Dakota Department of Health (DOH), Office of Health Facilities Licensure and Certification',
                'services_offered': 'Personal care, respite, homemaker, and assisted living services',
                'unique_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must be listed on the South Dakota Nurse Aide Registry; must work as a nurse aide in a paid position within 24 months to stay active on the registry; reciprocity available for out-of-state nurse aides with equivalent training and recent employment',
                'annual_training_requirements': '12 hours annual in-service/continuing education required to maintain certification',
                'effective_date': '2024-01-01',
                'registry_name': 'South Dakota Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Assisted Living Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical) of state-approved HHA training program; must pass written and skills competency evaluation; must be at least 18 years old; must be able to speak and understand English; must pass criminal background check and abuse/neglect registry check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://doh.sd.gov/boards/nursing/',
                'phone': '(605) 362-2760',
                'email': 'assistedliving@state.sd.us'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated South Dakota waiver programs')) 