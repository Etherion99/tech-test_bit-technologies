from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import PropertyType


@receiver(post_migrate)
def populate_property_types(sender, **kwargs):
    if sender.name == 'real_state':
        property_types = ['House', 'Apartment', 'Office']

        for type_name in property_types:
            PropertyType.objects.get_or_create(name=type_name)
