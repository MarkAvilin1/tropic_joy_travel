from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administration.urls')),
    path('trips/', include('offers.urls'))
]
