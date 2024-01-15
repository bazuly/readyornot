from django.shortcuts import render, redirect
from .models import UploadCarData
from .forms import CarForm

"""
Добавление данных на транспортное средство
"""


def add_car_data(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_data = UploadCarData()
            car_data.car_name = car_form.cleaned_data['car_name']
            car_data.car_number = car_form.cleaned_data['car_number']
            car_data.trailer_name = car_form.cleaned_data['trailer_name']
            car_data.trailer_number = car_form.cleaned_data['trailer_number']
            car_data.scan_doc = request.FILES.get('scan_doc')
            
            car_data.save()
            
            print('Data saved successfully')
            
            return redirect('add_car_data:add_car_data')
        else:
            print('Form is not valid', car_form.errors)
        
    else:
        car_form = CarForm()
            
    return render(request, 'add_car_data/add_car_data.html', {'car_form': car_form})