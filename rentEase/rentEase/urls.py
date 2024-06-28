from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('real-state/', include('real_state_frontend.urls')),
    path('real-state-api/', include('real_state.urls'))
]
