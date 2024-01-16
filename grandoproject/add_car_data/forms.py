from django import forms
from .models import UploadCarData


class CarForm(forms.ModelForm):
    class Meta:
        model = UploadCarData
        fields =['car_name', 'car_number', 'trailer_name', 'trailer_number', 'car_scan_doc', 'trailer_scan_doc']
