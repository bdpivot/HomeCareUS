from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates New Hampshire waiver programs'

    def handle(self, *args, **kwargs):
        new_hampshire = State.objects.get(abbreviation='NH')
        
        waiver_programs = [
            {
                'state': new_hampshire,
                'program_name': 'New Hampshire Medicaid Home Health Services',
                'administering_agency': 'New Hampshire Department of Health and Human Services (DHHS), Bureau of Health Facilities Administration',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; must be employed by a licensed agency for Medicaid/Medicare reimbursement',
                'annual_training_requirements': '24 hours continuing education every two years (or pass clinical and written competency test); 200 hours of active LNA work every two years required',
                'effective_date': '2024-01-01',
                'registry_name': 'New Hampshire Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must be a Licensed Nursing Assistant (LNA) before HHA certification, complete 100 total hours HHA training (60 theoretical, 40 clinical), pass written and practical skills certification exam, demonstrate competence in at least five patient care skills during clinical exam, have high school diploma or GED, pass criminal background check, and be listed on the New Hampshire Nurse Aide Registry',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dhhs.nh.gov/programs-services/adult-aging-care/nhcarepath/nhcarepath-home-care-information',
                'phone': '(603) 271-9499',
                'email': 'nhcarepath@dhhs.nh.gov'
            },
            {
                'state': new_hampshire,
                'program_name': 'Choices for Independence (CFI) Waiver',
                'administering_agency': 'New Hampshire Department of Health and Human Services (DHHS)',
                'services_offered': 'Personal care, homemaker, respite, skilled nursing, home modifications',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI; participant can reside at home, loved one\'s home, adult family home, or assisted living',
                'annual_training_requirements': '24 hours continuing education every two years (or pass clinical and written competency test); 200 hours of active LNA work every two years required',
                'effective_date': '2024-01-01',
                'registry_name': 'New Hampshire Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CFI Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a Licensed Nursing Assistant (LNA) before HHA certification, complete 100 total hours HHA training (60 theoretical, 40 clinical), pass written and practical skills certification exam, demonstrate competence in at least five patient care skills during clinical exam, have high school diploma or GED, pass criminal background check, and be listed on the New Hampshire Nurse Aide Registry',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.dhhs.nh.gov/programs-services/adult-aging-care/nh-choices-independence-waiver-renewal-and-amendments-2022-0',
                'phone': '(603) 271-9499',
                'email': 'nhcarepath@dhhs.nh.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated New Hampshire waiver programs')) 