from django.db import models
import os
from django.core.validators import FileExtensionValidator


"""
Добавление данных транспортых средств
"""


class UploadCarData(models.Model):
    car_name = models.CharField(max_length=50, null=True, blank=True)
    car_number = models.CharField(max_length=48, null=True, blank=True)

    # optional
    trailer_name = models.CharField(null=True, max_length=24, blank=True)
    trailer_number = models.CharField(max_length=48,
                                      null=True,
                                      blank=True
                                      )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    car_scan_doc = models.FileField(blank=True, null=True,
                                upload_to='car_data/',
                                validators=[FileExtensionValidator(allowed_extensions=['zip'])])
    
    trailer_scan_doc = models.FileField(blank=True, null=True,
                                upload_to='trailer_data/',
                                validators=[FileExtensionValidator(allowed_extensions=['zip'])])
    

    def save(self, *args, **kwargs):
        if self.car_scan_doc:
            filename = os.path.basename(self.car_scan_doc.name)
            folder_path = os.path.join('car_data', self.car_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            self.car_scan_doc.name = os.path.join(folder_path, filename)

        
        elif self.trailer_scan_doc:
            filename = os.path.basename(self.trailer_scan_doc.name)
            folder_path = os.path.join('trailer_data', self.trailer_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            self.trailer_scan_doc.name = os.path.join(folder_path, filename)

        
        super().save(*args, **kwargs)    
        
        
    def has_file(self):
        return bool(self.files) and os.path.exists(self.files.path)
    
    def __str__(self):
        return f'Данные на трансортное средство {self.car_number} добавлены'
    