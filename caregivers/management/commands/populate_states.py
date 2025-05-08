from django.core.management.base import BaseCommand
from caregivers.models import State

class Command(BaseCommand):
    help = 'Populates the states database with all US states'

    def handle(self, *args, **kwargs):
        states_data = [
            {'name': 'Alabama', 'abbreviation': 'AL', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Alaska', 'abbreviation': 'AK', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Arizona', 'abbreviation': 'AZ', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Arkansas', 'abbreviation': 'AR', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'California', 'abbreviation': 'CA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Colorado', 'abbreviation': 'CO', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Connecticut', 'abbreviation': 'CT', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Delaware', 'abbreviation': 'DE', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Florida', 'abbreviation': 'FL', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Georgia', 'abbreviation': 'GA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Hawaii', 'abbreviation': 'HI', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Idaho', 'abbreviation': 'ID', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Illinois', 'abbreviation': 'IL', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Indiana', 'abbreviation': 'IN', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Iowa', 'abbreviation': 'IA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Kansas', 'abbreviation': 'KS', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Kentucky', 'abbreviation': 'KY', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Louisiana', 'abbreviation': 'LA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Maine', 'abbreviation': 'ME', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Maryland', 'abbreviation': 'MD', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Massachusetts', 'abbreviation': 'MA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Michigan', 'abbreviation': 'MI', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Minnesota', 'abbreviation': 'MN', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Mississippi', 'abbreviation': 'MS', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Missouri', 'abbreviation': 'MO', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Montana', 'abbreviation': 'MT', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Nebraska', 'abbreviation': 'NE', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Nevada', 'abbreviation': 'NV', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'New Hampshire', 'abbreviation': 'NH', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'New Jersey', 'abbreviation': 'NJ', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'New Mexico', 'abbreviation': 'NM', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'New York', 'abbreviation': 'NY', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'North Carolina', 'abbreviation': 'NC', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'North Dakota', 'abbreviation': 'ND', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Ohio', 'abbreviation': 'OH', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Oklahoma', 'abbreviation': 'OK', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Oregon', 'abbreviation': 'OR', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Pennsylvania', 'abbreviation': 'PA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Rhode Island', 'abbreviation': 'RI', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'South Carolina', 'abbreviation': 'SC', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'South Dakota', 'abbreviation': 'SD', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Tennessee', 'abbreviation': 'TN', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Texas', 'abbreviation': 'TX', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Utah', 'abbreviation': 'UT', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Vermont', 'abbreviation': 'VT', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Virginia', 'abbreviation': 'VA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Washington', 'abbreviation': 'WA', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'West Virginia', 'abbreviation': 'WV', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Wisconsin', 'abbreviation': 'WI', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
            {'name': 'Wyoming', 'abbreviation': 'WY', 'allows_family_caregivers': True, 'has_consumer_directed_option': True},
        ]

        for state_data in states_data:
            State.objects.get_or_create(
                abbreviation=state_data['abbreviation'],
                defaults=state_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated states database')) 