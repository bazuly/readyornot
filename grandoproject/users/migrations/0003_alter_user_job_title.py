# Generated by Django 5.0.1 on 2024-02-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_photo_alter_user_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(blank=True, choices=[('Диспетчер-логист', 'Диспетчер-логист'), ('Специалист по маршрутизации', 'Специалист по маршрутизации'), ('Менеджер по сопровождению клиентов', 'Менеджер по сопровождению клиентов'), ('Менеджер по логистике', 'Менеджер по логистике'), ('Специалист отдела логистики', 'Специалист отдела логистики'), ('Директор транспортного отдела', 'Директор транспортного отдела')], max_length=128, null=True, verbose_name='Должность'),
        ),
    ]
