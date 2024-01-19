from django.shortcuts import render, redirect
from .models import UploadCarData, UploadTrailerData
from .forms import CarForm, TrailerForm

"""
Добавление данных на транспортное средство
"""


def add_car_data(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES, prefix='car')
        trailer_form = TrailerForm(request.POST, request.FIELS, prefix='trailer')
        if car_form.is_valid() and trailer_form.is_valid():
            car_data = UploadCarData(
                car_name=car_form.cleaned_data['car_name'],
                car_number=car_form.cleaned_data['car_number'],
                car_scan_doc=request.FILES.get('car_scan_doc')
            )
            car_data.save()
            
            print('car data saved successfully')
            
            trailer_data = UploadTrailerData(
                trailer_name=trailer_form.cleaned_data['trailer_name'],
                trailer_number=trailer_form.cleaned_data['trailer_number'],
                trailer_scan_doc=request.FILES.get('trailer_scan_doc')
            )
            trailer_data.save()
            
            print('trailer data saved successfully')
            
            return redirect('add_car_data:add_car_data')
        else:
            print('Form is not valid', car_form.errors, trailer_form.errors)

    else:
        car_form = CarForm(prefix='car')
        trailer_form = TrailerForm(prefix='trailer')

    return render(request, 'add_car_data/add_car_data.html', {'car_form': car_form, 'trailer_form': trailer_form})
            
