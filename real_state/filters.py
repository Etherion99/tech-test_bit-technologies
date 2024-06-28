import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = {
            'name': ['icontains'],
            'address': ['icontains'],
            'city': ['icontains'],
            'country': ['icontains'],
            'postal_code': ['icontains'],
            'area': ['gte', 'lte'],
            'type': ['exact']
        }
