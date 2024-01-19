# Generated by Django 5.0 on 2024-01-19 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_car_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadTrailerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailer_name', models.CharField(blank=True, max_length=24, null=True)),
                ('trailer_number', models.CharField(blank=True, max_length=48, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('trailer_scan_doc', models.FileField(blank=True, null=True, upload_to='trailer_data/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])])),
            ],
        ),
        migrations.RenameField(
            model_name='uploadcardata',
            old_name='scan_doc',
            new_name='car_scan_doc',
        ),
        migrations.RemoveField(
            model_name='uploadcardata',
            name='trailer_name',
        ),
        migrations.RemoveField(
            model_name='uploadcardata',
            name='trailer_number',
        ),
        migrations.AlterField(
            model_name='uploadcardata',
            name='car_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='uploadcardata',
            name='car_number',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
    ]
