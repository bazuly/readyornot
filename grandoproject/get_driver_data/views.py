from django.shortcuts import render, get_object_or_404
from add_driver_data.models import UploadDriverData
from django.http import FileResponse



"""
Получение данных водителей
Весь список
"""


def get_driver_data(request):
    driver_data = UploadDriverData.objects.all()
    context = {'driver_data': driver_data}
    
    return render(request, 'get_driver_data/get_driver_data.html', context)


def download_driver_data(request, driver_id):
    driver_data = get_object_or_404(UploadDriverData, pk=driver_id)
    file_path = driver_data.files.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response

