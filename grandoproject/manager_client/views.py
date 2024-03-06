from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ClientForm
from .models import Client
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/new_client.html'
    success_url = reverse_lazy('manager_client:new_client_success')

    
def new_client_success(request):
    return render(request,
                  'client/new_client_success.html')


@login_required
def get_client_data(request):
    client_data = Client.objects.all()
    
    items_per_page = 1
    paginator = Paginator(client_data, items_per_page)
    
    page = request.GET.get('page')
    try:
        client_data = paginator.page(page)
        
    except PageNotAnInteger:
        client_data = paginator.page(1)
        
    except EmptyPage:
        client_data = paginator.page(paginator.num_pages)
    
    context = {
        'client_data': client_data
        }
    
    return render(request, 'client/list_client.html', context)

# !!! Сделатьь нормальный поиск, с автокомплитом, как я реализовал в отчете
@login_required
def search_client(request):
    query = request.GET.get('q')
    
    if query:
        clients = Client.objects.filter(
            Q(name__icontains=query) |
            Q(manager__icontains=query) 
        )
    else:
        clients = Client.objects.all()
    
    context = {
        'client_data': clients,
        'query': query
    }
    
    return render(request, 'client/list_client.html', context)
