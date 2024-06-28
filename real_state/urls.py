from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyTypeViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'property-types', PropertyTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]