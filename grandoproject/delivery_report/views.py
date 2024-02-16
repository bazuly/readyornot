from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import DeliveryReport
from .forms import DeliveryReportForm
from django.contrib import messages


@login_required
def create_delivery_report(request):
    if request.method == 'POST':
        delivery_form = DeliveryReportForm(request.POST)
        if delivery_form.is_valid():
            try:
                delivery_report = DeliveryReport(
                    direction=delivery_form.cleaned_data['direction'],
                    driver_name=delivery_form.cleaned_data['driver_name'],
                    commentary=delivery_form.cleaned_data['commentary'],
                    dispatcher=delivery_form.cleaned_data['dispatcher']
                )

                delivery_report.save()

                messages.success(request, 'Отчет успешно создан')

                return HttpResponseRedirect(reverse('delivery_report:delivery_report_history'))
            except Exception as e:
                print(f'Error saving data: {e}')
                messages.error(request, 'Произошла ошибка при сохранении отчета.')
    else:
        delivery_form = DeliveryReportForm()

    return render(request, 'delivery_report/delivery_report_create.html', {'delivery_form': delivery_form})


@login_required
def delivery_report_history(request):
    delivery_report_history_data = DeliveryReport.objects.all()

    context = {'delivery_report_history_data': delivery_report_history_data}
    return render(request, 'delivery_report/delivery_report_history.html', context)
