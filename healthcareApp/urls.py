from django.urls import path
from .views import homePage, Page2, Page3, equipment

app_name = 'healthcareApp'

urlpatterns = [
    path('', homePage, name='home'),
    path('page2', Page2, name='page2'),
    path('page3', Page3, name='page3'),
    path('equipment/', equipment, name='equipment')
]