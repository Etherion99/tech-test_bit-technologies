import requests

from django.shortcuts import render

# Frontend views
real_state_api = 'http://localhost:8000/real-state-api'


def property_list(request):
    filters = request.GET.dict()
    properties_response = requests.get(f'{real_state_api}/properties/', params=filters)
    properties = properties_response.json() if properties_response.status_code == 200 else []

    property_types_response = requests.get(f'{real_state_api}/property-types/')
    property_types = property_types_response.json() if property_types_response.status_code == 200 else []

    return render(request, 'properties.html', {'properties': properties, 'property_types': property_types, 'filters': filters})
