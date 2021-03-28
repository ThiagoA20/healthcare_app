from django.shortcuts import render
from healthcareApp.models import Facility

def homePage(request):
    return render(request, 'index.html')

def facilities_detail_view(request):
    facilities = Facility.objects.all()
    print(facilities)
    args = {'facilities': facilities}
    return render(request, '../templates/index.html', args)
