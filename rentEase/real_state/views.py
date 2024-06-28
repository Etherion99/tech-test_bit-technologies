from rest_framework import viewsets
from .models import Property, PropertyType
from .serializers import PropertySerializer, PropertyTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PropertyFilter


# API views
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
