from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Arizona waiver programs'

    def handle(self, *args, **kwargs):
        arizona = State.objects.get(abbreviation='AZ')
        
        waiver_programs = [
            {
                'state': arizona,
                'program_name': 'Arizona Health Care Cost Containment System (AHCCCS)',
                'administering_agency': 'Arizona Health Care Cost Containment System',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '75 total hours (16 clinical hours) required for Licensed Health Aide certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Arizona Board of Nursing LHA Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for AHCCCS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete state-approved Licensed Health Aide (LHA) Training Program and obtain LHA license from Arizona Board of Nursing',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'AHCCCS Training Portal, Arizona Board of Nursing LHA Training',
                'website': 'https://www.azahcccs.gov/',
                'phone': '(602) 417-4000',
                'email': 'ahcccs@azahcccs.gov'
            },
            {
                'state': arizona,
                'program_name': 'ALTCS - Developmental Disabilities (ALTCS-DD)',
                'administering_agency': 'Arizona Health Care Cost Containment System',
                'services_offered': 'Personal care, habilitation, respite care, supported employment, day habilitation, home modifications, specialized medical equipment',
                'unique_requirements': 'Must have developmental disability, meet ICF/IID level of care, and have income below 300% of SSI',
                'annual_training_requirements': '75 total hours (16 clinical hours) required for Licensed Health Aide certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Arizona Board of Nursing LHA Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for ALTCS-DD, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete state-approved Licensed Health Aide (LHA) Training Program and obtain LHA license from Arizona Board of Nursing',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'AHCCCS Training Portal, Arizona Board of Nursing LHA Training',
                'website': 'https://www.azahcccs.gov/Members/ALTCS/',
                'phone': '(602) 417-4000',
                'email': 'altcs@azahcccs.gov'
            },
            {
                'state': arizona,
                'program_name': 'ALTCS - Elderly and Physical Disabilities (ALTCS-EPD)',
                'administering_agency': 'Arizona Health Care Cost Containment System',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, emergency response system',
                'unique_requirements': 'Must be 65 or older or have physical disability, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '75 total hours (16 clinical hours) required for Licensed Health Aide certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Arizona Board of Nursing LHA Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for ALTCS-EPD, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete state-approved Licensed Health Aide (LHA) Training Program and obtain LHA license from Arizona Board of Nursing',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'AHCCCS Training Portal, Arizona Board of Nursing LHA Training',
                'website': 'https://www.azahcccs.gov/Members/ALTCS/',
                'phone': '(602) 417-4000',
                'email': 'altcs@azahcccs.gov'
            },
            {
                'state': arizona,
                'program_name': 'Arizona Children\'s Rehabilitative Services (CRS)',
                'administering_agency': 'Arizona Health Care Cost Containment System',
                'services_offered': 'Personal care, habilitation, respite care, supported employment, day habilitation, home modifications, specialized medical equipment, Private Duty Nursing',
                'unique_requirements': 'Must be under 21, have qualifying medical condition, and have income below 300% of SSI',
                'annual_training_requirements': '75 total hours (16 clinical hours) required for Licensed Health Aide certification',
                'effective_date': '2024-01-01',
                'registry_name': 'Arizona Board of Nursing LHA Registry',
                'registry_update_frequency': 'Monthly',
                'required_forms': 'Application for CRS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Family members (including parents/guardians) may serve as Licensed Health Aides after training and licensure',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.50,
                'salary_range_max': 18.50,
                'free_training_available': True,
                'free_training_programs': 'AHCCCS Training Portal, Arizona Board of Nursing LHA Training',
                'website': 'https://www.azahcccs.gov/Members/CRS/',
                'phone': '(602) 417-4000',
                'email': 'crs@azahcccs.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Arizona waiver programs')) 