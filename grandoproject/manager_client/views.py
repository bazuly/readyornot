from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ClientForm
from .models import Client

""" 
Разобраться какого хера работает только по таким здоровым путевым ссылкам
Хуета какаета чес слово
"""


# @login_required
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = '/home/bazuly/developer/readyornot/grandoproject/manager_client/templates/сlient/new_client.html'
    success_url = reverse_lazy('manager_client:new_client_success')


def new_client_success(request):
    return render(request,
                  '/home/bazuly/developer/readyornot/grandoproject/manager_client/templates/сlient/new_client_success.html')

@login_required
def get_client_data(request):
    client_data = Client.objects.all()
    context = {'client_data': client_data}

    return render(request,
                  '/home/bazuly/developer/readyornot/grandoproject/manager_client/templates/сlient/list_client.html',
                  context)
