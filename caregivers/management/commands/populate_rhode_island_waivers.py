from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Rhode Island waiver programs'

    def handle(self, *args, **kwargs):
        rhode_island = State.objects.get(abbreviation='RI')
        
        waiver_programs = [
            {
                'state': rhode_island,
                'program_name': 'Rhode Island Medicaid Home Health Services',
                'administering_agency': 'Rhode Island Department of Health (RIDOH), Center for Health Facilities Regulation',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must complete 100 hours CNA training (80 hours classroom, 20 hours clinical); must pass CNA competency exam (written and skills, online proctoring available); must be listed on the Rhode Island Nurse Aide Registry; must be employed by a licensed Home Nursing Care Provider or Home Care Provider agency; agencies must meet statewide community standard for uncompensated care; agencies must submit notarized listing of all direct/indirect owners and officers for licensure; public comment period required for new/transfer license applications',
                'annual_training_requirements': 'Ongoing license renewal and biweekly supervisory visits required',
                'effective_date': '2024-01-01',
                'registry_name': 'Rhode Island Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 100 hours CNA training (80 hours classroom, 20 hours clinical); must pass CNA competency exam; must pass criminal background check; must demonstrate competency assessment; must have physical ability to perform aide duties',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.ri.gov/home-healthcare',
                'phone': '(401) 222-5200',
                'email': 'health.licensing@health.ri.gov'
            },
            {
                'state': rhode_island,
                'program_name': 'Managed Long-Term Services and Supports (MLTSS) – 1115 Comprehensive Demonstration Waiver',
                'administering_agency': 'Rhode Island Department of Health (RIDOH), Center for Health Facilities Regulation',
                'services_offered': 'Respite, personal care, homemaker, skilled nursing, and other supports',
                'unique_requirements': 'All former 1915(c) waivers now consolidated into 1115 MLTSS Comprehensive Demonstration Waiver; must complete 100 hours CNA training (80 hours classroom, 20 hours clinical); must pass CNA competency exam (written and skills, online proctoring available); must be listed on the Rhode Island Nurse Aide Registry; must be employed by a licensed Home Nursing Care Provider or Home Care Provider agency; agencies must meet statewide community standard for uncompensated care; agencies must submit notarized listing of all direct/indirect owners and officers for licensure; public comment period required for new/transfer license applications',
                'annual_training_requirements': 'Ongoing license renewal and biweekly supervisory visits required',
                'effective_date': '2024-01-01',
                'registry_name': 'Rhode Island Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for MLTSS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 hours CNA training (80 hours classroom, 20 hours clinical); must pass CNA competency exam; must pass criminal background check; must demonstrate competency assessment; must have physical ability to perform aide duties',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://health.ri.gov/home-healthcare',
                'phone': '(401) 222-5200',
                'email': 'mltss@health.ri.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Rhode Island waiver programs')) 