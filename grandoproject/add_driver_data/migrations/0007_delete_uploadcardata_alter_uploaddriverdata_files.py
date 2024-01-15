# Generated by Django 5.0 on 2024-01-11 15:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_driver_data', '0006_rename_car_num_uploadcardata_car_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadCarData',
        ),
        migrations.AlterField(
            model_name='uploaddriverdata',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])]),
        ),
    ]
