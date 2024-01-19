from django import forms
from .models import UploadCarData, UploadTrailerData


class CarForm(forms.ModelForm):
    class Meta:
        model = UploadCarData
        fields = ['car_name', 'car_number','car_scan_doc']
        

class TrailerForm(forms.ModelForm):
    class Meta:
        model = UploadTrailerData
        fields = ['trailer_name', 'trailer_number', 'trailer_scan_doc']