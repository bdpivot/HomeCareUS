from django.db import migrations

def create_initial_data(apps, schema_editor):
    State = apps.get_model('caregivers', 'State')
    CertificationType = apps.get_model('caregivers', 'CertificationType')

    # Create States
    states_data = [
        {
            'name': 'New York',
            'code': 'NY',
            'training_hours_required': 125,
            'renewal_cycle_months': 12,
            'requires_background_check': True,
            'requires_fingerprinting': True,
            'requires_medicaid_cert': True,
            'requires_surety_bond': True,
            'min_bond_amount': 10000.00
        },
        {
            'name': 'Georgia',
            'code': 'GA',
            'training_hours_required': 40,
            'renewal_cycle_months': 24,
            'requires_background_check': True,
            'requires_fingerprinting': False,
            'requires_medicaid_cert': False,
            'requires_surety_bond': False,
            'min_bond_amount': None
        },
        {
            'name': 'Washington',
            'code': 'WA',
            'training_hours_required': 75,
            'renewal_cycle_months': 12,
            'requires_background_check': True,
            'requires_fingerprinting': False,
            'requires_medicaid_cert': True,
            'requires_surety_bond': False,
            'min_bond_amount': None
        }
    ]

    for state_data in states_data:
        State.objects.create(**state_data)

    # Create Certification Types
    cert_types_data = [
        {
            'name': 'Personal Care Aide (PCA)',
            'description': 'Basic personal care and assistance certification',
            'is_medicaid_certified': False,
            'is_hospice_certified': False,
            'is_private_duty': True,
            'required_training_hours': 40,
            'renewal_cycle_months': 12
        },
        {
            'name': 'Home Health Aide (HHA)',
            'description': 'Advanced home health care certification',
            'is_medicaid_certified': True,
            'is_hospice_certified': False,
            'is_private_duty': True,
            'required_training_hours': 75,
            'renewal_cycle_months': 12
        },
        {
            'name': 'Certified Nursing Assistant (CNA)',
            'description': 'Nursing assistant certification',
            'is_medicaid_certified': True,
            'is_hospice_certified': True,
            'is_private_duty': True,
            'required_training_hours': 120,
            'renewal_cycle_months': 24
        },
        {
            'name': 'Hospice Care Certification',
            'description': 'Specialized hospice care certification',
            'is_medicaid_certified': True,
            'is_hospice_certified': True,
            'is_private_duty': True,
            'required_training_hours': 16,
            'renewal_cycle_months': 12
        }
    ]

    for cert_type_data in cert_types_data:
        CertificationType.objects.create(**cert_type_data)

def remove_initial_data(apps, schema_editor):
    State = apps.get_model('caregivers', 'State')
    CertificationType = apps.get_model('caregivers', 'CertificationType')
    
    State.objects.all().delete()
    CertificationType.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('caregivers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, remove_initial_data),
    ] 