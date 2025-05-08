from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Georgia waiver programs'

    def handle(self, *args, **kwargs):
        georgia = State.objects.get(abbreviation='GA')
        
        waiver_programs = [
            {
                'state': georgia,
                'program_name': 'Georgia Medicaid Home Health Services',
                'administering_agency': 'Georgia Department of Community Health (DCH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based or state-approved training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 10.00,
                'salary_range_max': 15.00,
                'free_training_available': True,
                'free_training_programs': 'DCH Training Portal, State-approved HHA training programs',
                'website': 'https://dch.georgia.gov/providers/provider-types/home-health-services',
                'phone': '(404) 656-4507',
                'email': 'dch.healthcarefacilityregulation@dch.ga.gov'
            },
            {
                'state': georgia,
                'program_name': 'Community Care Services Program (CCSP) Waiver',
                'administering_agency': 'Georgia Department of Community Health (DCH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be elderly or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CCSP, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based or state-approved training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 10.50,
                'salary_range_max': 15.50,
                'free_training_available': True,
                'free_training_programs': 'DCH Training Portal, State-approved HHA training programs',
                'website': 'https://dch.georgia.gov/divisionsoffices/hfrd/facilities-provider-information/private-home-care-program',
                'phone': '(404) 656-4507',
                'email': 'dch.ccsp@dch.ga.gov'
            },
            {
                'state': georgia,
                'program_name': 'SOURCE Waiver',
                'administering_agency': 'Georgia Department of Community Health (DCH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be elderly or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for SOURCE, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based or state-approved training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.00,
                'salary_range_max': 16.00,
                'free_training_available': True,
                'free_training_programs': 'DCH Training Portal, State-approved HHA training programs',
                'website': 'https://dch.georgia.gov/divisionsoffices/hfrd/facilities-provider-information/private-home-care-program',
                'phone': '(404) 656-4507',
                'email': 'dch.source@dch.ga.gov'
            },
            {
                'state': georgia,
                'program_name': 'Independent Care Waiver Program (ICWP)',
                'administering_agency': 'Georgia Department of Community Health (DCH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be physically disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for ICWP, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based or state-approved training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 11.50,
                'salary_range_max': 16.50,
                'free_training_available': True,
                'free_training_programs': 'DCH Training Portal, State-approved HHA training programs',
                'website': 'https://dch.georgia.gov/divisionsoffices/hfrd/facilities-provider-information/private-home-care-program',
                'phone': '(404) 656-4507',
                'email': 'dch.icwp@dch.ga.gov'
            },
            {
                'state': georgia,
                'program_name': 'Georgia Pediatric Program (GAPP)',
                'administering_agency': 'Georgia Department of Community Health (DCH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be medically fragile child, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'No central registry; agencies maintain records',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for GAPP, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 75 total hours (16 clinical hours) of agency-based or state-approved training, pass competency evaluation, and pass background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'DCH Training Portal, State-approved HHA training programs',
                'website': 'https://dch.georgia.gov/divisionsoffices/hfrd/facilities-provider-information/private-home-care-program',
                'phone': '(404) 656-4507',
                'email': 'dch.gapp@dch.ga.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Georgia waiver programs')) 