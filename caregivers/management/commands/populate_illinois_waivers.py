from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Illinois waiver programs'

    def handle(self, *args, **kwargs):
        illinois = State.objects.get(abbreviation='IL')
        
        waiver_programs = [
            {
                'state': illinois,
                'program_name': 'Illinois Medicaid Home Health Services',
                'administering_agency': 'Illinois Department of Public Health (IDPH)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must meet nursing home level of care and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Illinois Health Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Medicaid Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, pass background check, and have high school diploma or GED',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 12.00,
                'salary_range_max': 17.00,
                'free_training_available': True,
                'free_training_programs': 'IDPH Training Portal, State-approved HHA training programs',
                'website': 'https://dph.illinois.gov/topics-services/health-care-regulation/health-care-facilities/home-health.html',
                'phone': '(217) 782-2913',
                'email': 'dph.homehealth@illinois.gov'
            },
            {
                'state': illinois,
                'program_name': 'Community Care Program (CCP)',
                'administering_agency': 'Illinois Department on Aging (IDoA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be elderly, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Illinois Health Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for CCP, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, pass background check, and have high school diploma or GED',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 12.50,
                'salary_range_max': 17.50,
                'free_training_available': True,
                'free_training_programs': 'IDPH Training Portal, State-approved HHA training programs',
                'website': 'https://ilaging.illinois.gov/forprofessionals/training.html',
                'phone': '(800) 252-8966',
                'email': 'aging.illinois.gov@illinois.gov'
            },
            {
                'state': illinois,
                'program_name': 'In-Home Care Program / Medicaid Waiver (AABD)',
                'administering_agency': 'Illinois Department of Human Services (DHS) and Department on Aging (DoA)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment',
                'unique_requirements': 'Must be elderly or disabled, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2024-01-01',
                'registry_name': 'Illinois Health Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for AABD, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete 120 classroom hours and 40 clinical hours of state-approved HHA training, pass HHA competency exam, pass background check, and have high school diploma or GED',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 13.00,
                'salary_range_max': 18.00,
                'free_training_available': True,
                'free_training_programs': 'IDPH Training Portal, State-approved HHA training programs',
                'website': 'https://www.dhs.state.il.us/page.aspx?item=18142',
                'phone': '(800) 843-6154',
                'email': 'dhs.aabd@illinois.gov'
            },
            {
                'state': illinois,
                'program_name': 'Certified Family Health Aide Program',
                'administering_agency': 'Illinois Department of Healthcare and Family Services (HFS)',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be medically fragile/technology-dependent child, meet nursing home level of care, and have income below 300% of SSI',
                'annual_training_requirements': '12 hours annual in-service/continuing education required',
                'effective_date': '2027-01-01',
                'registry_name': 'Illinois Health Care Worker Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for Certified Family Health Aide, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must complete special state training and certification for family caregivers, pass background check, and have high school diploma or GED',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': False,
                'salary_range_min': 40.00,
                'salary_range_max': 40.00,
                'free_training_available': True,
                'free_training_programs': 'HFS Training Portal, State-approved family caregiver training programs',
                'website': 'https://hfs.illinois.gov/medicalclients/hcbs.html',
                'phone': '(877) 912-8880',
                'email': 'hfs.medicalclients@illinois.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Illinois waiver programs')) 