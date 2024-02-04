from django import forms
from .models import Client, Tag


class ClientForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Client
        fields = ['name', 'inn', 'contacts', 'manager', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

