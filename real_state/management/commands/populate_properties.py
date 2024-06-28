import random

from django.core.management.base import BaseCommand
from real_state.models import Property, PropertyType


class Command(BaseCommand):
    help = 'Populate properties in the database'

    def handle(self, *args, **kwargs):
        property_types = list(PropertyType.objects.all())

        properties = [
            {
                'name': 'Casa Bonita',
                'address': '1234 Calle Falsa',
                'country': 'España',
                'city': 'Madrid',
                'postal_code': '28001',
                'type': random.choice(property_types),
                'area': 120.50,
            },
            {
                'name': 'Apartamento Moderno',
                'address': '5678 Avenida Principal',
                'country': 'España',
                'city': 'Barcelona',
                'postal_code': '08001',
                'type': random.choice(property_types),
                'area': 80.00,
            },
            {
                'name': 'Oficina Central',
                'address': '91011 Gran Vía',
                'country': 'España',
                'city': 'Valencia',
                'postal_code': '46001',
                'type': random.choice(property_types),
                'area': 200.00,
            },
        ]

        for prop in properties:
            Property.objects.create(**prop)

        self.stdout.write(self.style.SUCCESS('Properties have been populated successfully.'))
