from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Hawaii waiver programs'

    def handle(self, *args, **kwargs):
        hawaii = State.objects.get(abbreviation='HI')
        
        waiver_programs = [
            {
                'state': hawaii,
                'program_name': 'Med-QUEST (Hawaii Medicaid Managed Care Program)',
                'administering_agency': 'Hawaii Department of Health (DOH), Office of Health Care Assurance (OHCA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Hawaii Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Med-QUEST, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 total hours (70 clinical hours) of CNA program, pass competency exam (written and skills), and pass background check with fingerprinting',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'OHCA Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://medquest.hawaii.gov/content/medquest/en/plans-providers/certification-programs.html',
                'phone': '(808) 692-8000',
                'email': 'medquest.ohca@doh.hawaii.gov'
            },
            {
                'state': hawaii,
                'program_name': 'Expanded Home and Community Based Services (HCBS) under Med-QUEST',
                'administering_agency': 'Hawaii Department of Health (DOH), Office of Health Care Assurance (OHCA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Hawaii Nurse Aide Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 100 total hours (70 clinical hours) of CNA program, pass competency exam (written and skills), and pass background check with fingerprinting',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'OHCA Training Portal, State-approved CNA/HHA training programs',
                'website': 'https://medquest.hawaii.gov/content/medquest/en/plans-providers/certification-programs.html',
                'phone': '(808) 692-8000',
                'email': 'medquest.hcbs@doh.hawaii.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Hawaii waiver programs')) 