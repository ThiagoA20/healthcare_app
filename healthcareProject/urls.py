from django.contrib import admin
from django.urls import path, include
from healthcareApp.views import facilities_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('healthcareApp.urls'), name='healthcareProject'),
    path('facilities', facilities_detail_view)
]
