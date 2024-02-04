from django.shortcuts import render
from .models import Client, Tag
from .forms import ClientForm, TagForm
from django.http import HttpResponseRedirect
from django.urls import reverse

"""
Добавление клиента
"""


def add_client(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST, prefix='client')
        if client_form.is_valid():
            trailer_data = Client(
                name=client_form.cleaned_data['name'],
                inn=client_form.cleaned_data['inn'],
                contacts=client_form.cleaned_data['contacts'],
                tag=client_form.cleaned_data['tag']

            )

            trailer_data.save()

            return HttpResponseRedirect(reverse('manager_client:manager_client'))

        else:
            print('Form in not valid', client_form.errors)

#
# def manager_clietns(request, client_id):
#     manager = Manager.objects.get(pk=client_id)
#     clients = manager.client_set.all()
#     context = {'clients': clients, 'manager': manager}
#     return render(request, 'manager_client.html', context)
