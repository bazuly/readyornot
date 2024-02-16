from .models import DeliveryReport
from django import forms


class DeliveryReportForm(forms.ModelForm):
    class Meta:
        model = DeliveryReport
        fields = ['direction', 'driver_name', 'commentary', 'client_list', 'dispatcher']

        widgets = {
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'commentary': forms.Textarea(attrs={'class': 'form-control'}),
            'client_list': forms.Select(attrs={'class': 'form-control'}),
            'dispatcher': forms.Select(attrs={'class': 'form-control'}),
        }

#
# # скорее всего надо будет реализовать возможность загрузки нескольких файлов
# class UnsuccessfulReportForm(forms.Form):
#     class Meta:
#         model = UnsuccessfulReport
#         fields = ['returned_client', 'returned_goods_description', 'returned_goods_photo']
#
#
# class SuccessReportForm(forms.Form):
#     class Meta:
#         model = SuccessReport
#         fields = []