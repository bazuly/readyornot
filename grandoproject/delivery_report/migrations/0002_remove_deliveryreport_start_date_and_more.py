# Generated by Django 5.0.1 on 2024-02-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryreport',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='deliveryreport',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='deliveryreport',
            name='client_list',
            field=models.TextField(choices=[('ТД Гроуми', 'ТД Гроуми'), ('Ярославский Бройлер', 'Ярославский Бройлер'), ('Останкино Новый Стандарт', 'Останкино Новый Стандарт'), ('Шпинат', 'Шпинат'), ('тест', 'тест')], max_length=256),
        ),
    ]