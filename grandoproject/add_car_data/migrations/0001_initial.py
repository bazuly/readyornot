# Generated by Django 5.0.1 on 2024-02-08 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCarData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(blank=True, max_length=50, null=True)),
                ('car_number', models.CharField(blank=True, max_length=48, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tonnage', models.FloatField(blank=True, choices=[(1.5, '1.5 тонны'), (2, '2 тонны'), (3, '3 тонны'), (5, '5 тонн'), (7, '7 тонн'), (10, '10 тонн'), (20, '20 тонн')], null=True)),
                ('capacity', models.IntegerField(null=True)),
                ('car_scan_doc', models.FileField(blank=True, null=True, upload_to='car_data/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])])),
            ],
        ),
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
    ]
