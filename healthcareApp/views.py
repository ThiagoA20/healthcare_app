from django.shortcuts import render
from healthcareApp.models import *

def homePage(request):
    return render(request, 'Page1.html')

def facilities_detail_view(request):
    facilities = Facility.objects.all()
    args = {'facilities': facilities}
    return render(request, '../templates/index.html', args)

def Mass_spectrometer_details(request):
    obj = Mass_spectrometer.objects.all()
    return render(request, '../templates/index.html', obj)

def equipment(request):
    # query = request.GET.get('Mass_spectrometer')
    # if query:
    #     results = Mass_spectrometer.objects.all()
    
    

    # context = RequestContext(request)
    equipment = Mass_spectrometer.objects.all()
    facilities = Facility.objects.all()
    args = {'equipment': equipment, 'facilities': facilities}
    return render(request, 'equipment.html', args)

def Page2(request):
    return render(request, 'Page2.html')

def Page3(request):
    return render(request, 'Page3.html')