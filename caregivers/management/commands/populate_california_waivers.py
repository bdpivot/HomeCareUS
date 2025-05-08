from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates California waiver programs'

    def handle(self, *args, **kwargs):
        california = State.objects.get(abbreviation='CA')
        
        waiver_programs = [
            {
                'state': california,
                'program_name': 'Medi-Cal',
                'administering_agency': 'California Department of Health Care Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI. Asset limit eliminated as of 2024, 30-month look-back phased out by July 2026',
                'annual_training_requirements': '12 hours annual in-service/continuing education required for renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'California Home Health Aide Registry (CDPH/ATCS)',
                'registry_update_frequency': 'Biennial renewal required',
                'required_forms': 'Application for Medi-Cal, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours (20 clinical hours) of state-approved HHA training, pass competency evaluation, and complete Live Scan fingerprinting',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.00,
                'salary_range_max': 20.00,
                'free_training_available': True,
                'free_training_programs': 'CDPH Training Portal, State-approved HHA training programs',
                'website': 'https://www.dhcs.ca.gov/services/medi-cal/Pages/default.aspx',
                'phone': '(916) 445-4171',
                'email': 'medi-cal@dhcs.ca.gov'
            },
            {
                'state': california,
                'program_name': 'Home and Community Based Alternatives (HCBA) Waiver',
                'administering_agency': 'California Department of Health Care Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, assistive technology, skilled nursing',
                'unique_requirements': 'Must be medically fragile/technology-dependent, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required for renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'California Home Health Aide Registry (CDPH/ATCS)',
                'registry_update_frequency': 'Biennial renewal required',
                'required_forms': 'Application for HCBA Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours (20 clinical hours) of state-approved HHA training, pass competency evaluation, and complete Live Scan fingerprinting',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 15.50,
                'salary_range_max': 20.50,
                'free_training_available': True,
                'free_training_programs': 'CDPH Training Portal, State-approved HHA training programs',
                'website': 'https://www.dhcs.ca.gov/services/Pages/medi-calwaivers.aspx',
                'phone': '(916) 445-4171',
                'email': 'hcba@dhcs.ca.gov'
            },
            {
                'state': california,
                'program_name': 'In-Home Supportive Services (IHSS)',
                'administering_agency': 'California Department of Social Services',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be aged, blind, or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required for renewal',
                'effective_date': '2024-01-01',
                'registry_name': 'Home Care Aide Registry (CDSS)',
                'registry_update_frequency': 'Biennial renewal required',
                'required_forms': 'Application for IHSS, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 total hours (20 clinical hours) of state-approved HHA training, pass competency evaluation, and complete Live Scan fingerprinting',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 14.50,
                'salary_range_max': 19.50,
                'free_training_available': True,
                'free_training_programs': 'CDSS Training Portal, State-approved HHA training programs',
                'website': 'https://www.cdss.ca.gov/in-home-supportive-services',
                'phone': '(916) 651-8848',
                'email': 'ihss@dss.ca.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated California waiver programs')) 