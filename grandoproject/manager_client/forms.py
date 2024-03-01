from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contacts', 'manager', 'main_email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contacts': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'main_email': forms.TextInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'main_email': 'Это строка для почты, на которую должен приходить отчет о доставке',
        }

        labels = {
            'name': 'Название клиента',
            'contacts': 'Контактная Информация',
            'manager': 'Менеджер',
            'main_email': 'Почта для рассылки',
        }
