from django.shortcuts import render, get_object_or_404
from add_car_data.models import UploadCarData, UploadTrailerData
from django.http import FileResponse

"""
Получение данных на транспортное средство
"""


def get_car_data(request):
    car_data = UploadCarData.objects.all()

    for data in car_data:
        data.has_file = data.has_file()

    context = {'car_data': car_data}

    return render(request, 'get_car_data/get_car_data.html', context)


# можно сделать лучше
def download_car_data(request, car_id):
    car_data = get_object_or_404(UploadCarData, pk=car_id)
    file_path = car_data.car_scan_doc.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


def get_trailer_data(request):
    trailer_data = UploadTrailerData.objects.all()

    for data in trailer_data:
        data.has_file = data.has_file()

    context = {'trailer_data': trailer_data}

    return render(request, 'get_car_data/get_trailer_data.html', context)


def download_trailer_data(request, trailer_id):
    trailer_data = get_object_or_404(UploadTrailerData, pk=trailer_id)
    file_path = trailer_data.trailer_scan_doc.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response
