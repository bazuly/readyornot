from django.db import models
# from delivery_report.models import DeliveryReport


class Client(models.Model):
    """Модель клиентов/поставщиков"""

    MANAGER_CHOICES = [
        ('Владимир Сороковой', 'Владимир Сороковой'),
        ('Наталья Пряхина', 'Наталья Пряхина'),
        ('Татьяна Петкун', 'Татьяна Петкун'),
        ('Марта Селиксар', 'Марта Селиксар'),
        ('Ольга Лаппо', 'Ольга Лаппо'),
        ('Екатерина Смышлякова', 'Екатерина Смышлякова'),
        ('Анастасия Тарассу', 'Анастасия Тарассу'),
        ('Алексей Зайцев', 'Алексей Зайцев'),
        ('Всеволод Родионов', 'Всеволод Родионов'),
        ('Перминова Надежда', 'Перминова Надежда'),
        ('Менедежры УК Грандо', 'Менедежры УК Грандо'),
    ]
    name = models.CharField(max_length=128, null=False)
    contacts = models.TextField(max_length=700)
    manager = models.CharField(max_length=128, blank=True, null=True, choices=MANAGER_CHOICES)
    main_email = models.EmailField(max_length=128, blank=True, null=True) # использовать для рассылки писем

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     DeliveryReport.CLIENT_NAME_CHOICES = [(client.name, client.name) for client in Client.objects.all()]

    def __str__(self):
        return self.name
