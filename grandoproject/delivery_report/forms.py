from .models import DeliveryReport, EmailReportToClientSuccess
from django import forms
from django_select2.forms import Select2MultipleWidget
from manager_client.models import Client


class DeliveryReportForm(forms.ModelForm):
    class Meta:
        model = DeliveryReport
        fields = ['direction', 'driver_name', 'commentary', 'client_list', 'dispatcher']

        widgets = {
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'commentary': forms.Textarea(attrs={'class': 'form-control'}),
            'client_list': Select2MultipleWidget(attrs={'class': 'form-control'}),
            'dispatcher': forms.Select(attrs={'class': 'form-control'}),
        }


class EmailReportToClientForm(forms.ModelForm):
    class Meta:
        model = EmailReportToClientSuccess
        fields = ['client', 'direction', 'message']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),

        }

        def __init__(self, *args, **kwargs):
            super(EmailReportToClientForm, self).__init__(*args, **kwargs)
            self.fields['client'].queryset = Client.objects.all()
            self.fields['message'].widget = forms.Textarea(attrs={'class': 'form-control'})

    # # скорее всего надо будет реализовать возможность загрузки нескольких файлов
# class UnsuccessfulReportForm(forms.Form):
#     class Meta:
#         model = UnsuccessfulReport
#         fields = ['returned_client', 'returned_goods_description', 'returned_goods_photo']
#
#
