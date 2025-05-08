from django.core.management.base import BaseCommand
from caregivers.models import State, StateWaiverProgram

class Command(BaseCommand):
    help = 'Populates Oregon waiver programs'

    def handle(self, *args, **kwargs):
        oregon = State.objects.get(abbreviation='OR')
        
        waiver_programs = [
            {
                'state': oregon,
                'program_name': 'Oregon Health Plan (OHP) – Medicaid Home Health Services',
                'administering_agency': 'Oregon Health Authority (OHA), Health Care Regulation and Quality Improvement',
                'services_offered': 'Personal care, homemaker services, respite care, adult day health, home-delivered meals, home modifications, medical supplies and equipment, skilled nursing',
                'unique_requirements': 'Must be a Certified Nursing Assistant (CNA) before HHA certification; 155 total hours for CNA training (at least 80 classroom, 75 clinical, including 27 hours labwork); must demonstrate competency in home health duties (infection control, documentation, reporting, environmental maintenance, client needs, etc.); must pass state-approved written and clinical competency exam; agency must provide skilled nursing and at least one other service; agency must have policies established by professional personnel (including at least two non-owner/non-employee clinicians and two consumers); agency must maintain clinical and financial records for all patients; agency must have an overall plan and budget in effect; agencies must submit administrator resume with licensure application',
                'annual_training_requirements': 'Continuing education requirements may apply (varies by role and employer)',
                'effective_date': '2024-01-01',
                'registry_name': 'Oregon State Board of Nursing CNA Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for OHP Home Health, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': False,
                'family_caregiver_requirements': 'Must be a Certified Nursing Assistant (CNA) before HHA certification; 155 total hours for CNA training (at least 80 classroom, 75 clinical, including 27 hours labwork); must demonstrate competency in home health duties; must pass state-approved written and clinical competency exam; must pass criminal background check',
                'has_consumer_directed_option': False,
                'has_self_directed_option': False,
                'has_agency_option': True,
                'salary_range_min': 16.00,
                'salary_range_max': 21.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.oregon.gov/oha/PH/PROVIDERPARTNERRESOURCES/HEALTHCAREPROVIDERSFACILITIES/HEALTHCAREHEALTHCAREREGULATIONQUALITYIMPROVEMENT/Documents/HHAApplication.pdf',
                'phone': '(971) 673-0540',
                'email': 'hha.info@oha.oregon.gov'
            },
            {
                'state': oregon,
                'program_name': 'Home and Community-Based Services (HCBS) Waivers',
                'administering_agency': 'Oregon Health Authority (OHA), Health Care Regulation and Quality Improvement',
                'services_offered': 'Personal care, respite, homemaker, home modifications, transportation, emergency response, and home-delivered meals',
                'unique_requirements': 'Must be a Certified Nursing Assistant (CNA) before HHA certification; 155 total hours for CNA training (at least 80 classroom, 75 clinical, including 27 hours labwork); must demonstrate competency in home health duties; must pass state-approved written and clinical competency exam; additional training/testing required for Personal Support Workers (PSW), Homecare Workers (HCW), and Personal Care Attendants (PCA) under Senate Bill 1534',
                'annual_training_requirements': 'Continuing education requirements may apply (varies by role and employer)',
                'effective_date': '2024-01-01',
                'registry_name': 'Oregon State Board of Nursing CNA Registry and OHCC Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for HCBS Waiver, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a Certified Nursing Assistant (CNA) before HHA certification; 155 total hours for CNA training (at least 80 classroom, 75 clinical, including 27 hours labwork); must demonstrate competency in home health duties; must pass state-approved written and clinical competency exam; must pass criminal background check',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 16.50,
                'salary_range_max': 21.50,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.oregon.gov/odhs/providers-partners/homecare-workforce/pages/default.aspx',
                'phone': '(971) 673-0540',
                'email': 'hcbs@oha.oregon.gov'
            },
            {
                'state': oregon,
                'program_name': 'Oregon Project Independence – Medicaid (OPI–M)',
                'administering_agency': 'Oregon Health Authority (OHA), Health Care Regulation and Quality Improvement',
                'services_offered': 'Personal care, respite, homemaker, home modifications, transportation, emergency response, and home-delivered meals',
                'unique_requirements': '1115 Demonstration Waiver (2024–2029); expands HCBS to those not meeting nursing facility level of care; allows continuous Medicaid eligibility for two years; supports unpaid caregivers with education/training; must be a Certified Nursing Assistant (CNA) before HHA certification; 155 total hours for CNA training (at least 80 classroom, 75 clinical, including 27 hours labwork); must demonstrate competency in home health duties; must pass state-approved written and clinical competency exam; additional training/testing required for Personal Support Workers (PSW), Homecare Workers (HCW), and Personal Care Attendants (PCA) under Senate Bill 1534',
                'annual_training_requirements': 'Continuing education requirements may apply (varies by role and employer)',
                'effective_date': '2024-01-01',
                'registry_name': 'Oregon State Board of Nursing CNA Registry and OHCC Registry',
                'registry_update_frequency': 'As needed',
                'required_forms': 'Application for OPI-M, Level of Care Assessment, Financial Assessment',
                'allows_family_caregivers': True,
                'family_caregiver_requirements': 'Must be a Certified Nursing Assistant (CNA) before HHA certification; 155 total hours for CNA training (at least 80 classroom, 75 clinical, including 27 hours labwork); must demonstrate competency in home health duties; must pass state-approved written and clinical competency exam; must pass criminal background check; Family Home Health Aide Program (proposed, SB1073, 2025): would certify family caregivers as Family Home Health Aides',
                'has_consumer_directed_option': True,
                'has_self_directed_option': True,
                'has_agency_option': True,
                'salary_range_min': 17.00,
                'salary_range_max': 22.00,
                'free_training_available': True,
                'free_training_programs': 'On-the-job training and approved programs available',
                'website': 'https://www.mcknightshomecare.com/news/cms-approves-1115-waiver-to-enhance-oregons-home-and-community-based-services/',
                'phone': '(971) 673-0540',
                'email': 'opi@oha.oregon.gov'
            }
        ]

        for waiver_data in waiver_programs:
            StateWaiverProgram.objects.get_or_create(
                state=waiver_data['state'],
                program_name=waiver_data['program_name'],
                defaults=waiver_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Oregon waiver programs')) 