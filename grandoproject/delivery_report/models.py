from django.db import models
from manager_client.models import Client


class DeliveryReport(models.Model):
    """ Модель отчета по доставке """

    CLIENT_NAME_CHOICES = [(client.name, client.name) for client in Client.objects.all()]
    DISPATCHER_CHOICES = [
        ('Ксения Майорова', 'Ксения Майорова'),
        ('Мазалов Максим', 'Мазалов Максим'),
        ('Тольев Алексей', 'Тольев Алексей'),
        ('Анна Нуруллова', 'Анна Нуруллова')
    ]

    direction = models.CharField(max_length=128, null=False)
    driver_name = models.CharField(max_length=128, null=False)
    commentary = models.TextField(max_length=256, blank=True, null=True)
    # Список перевозимых поставщиков
    client_list = models.TextField(max_length=256, choices=CLIENT_NAME_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    dispatcher = models.CharField(max_length=128, choices=DISPATCHER_CHOICES)

    def __str__(self):
        return f'Отчет по направлению {self.direction} успешно обновлен'


class EmailReportToClientSuccess(models.Model):
    """
    Модель используется для оповещения клиентов
    при успешной доставке груза
    """

    direction = models.CharField(max_length=128, null=False)
    message = models.TextField(max_length=1024, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Отчет клиентам: "{self.client}" успешно отправлен'

# class UnsuccessfulReport(models.Model):
#     """
#     Модель используется для оповещения клиентов и записи данных,
#     когда на ТТ есть возвратная продукция или возникают какие-либо проблемы
#     """
#     CLIENT_NAME_CHOICES = [(client.name, client.name) for client in Client.objects.all()]
#
#     returned_client = models.CharField(max_length=128, choices=CLIENT_NAME_CHOICES)
#     returned_goods_description = models.TextField(max_length=512, blank=True, null=True)
#     returned_goods_photo = models.ImageField(blank=True, null=True,
#                                              upload_to=f'returned_goods/{returned_client}/%Y/%m/%d/')
#     email_to_send = models.EmailField(max_length=128)
#
#     def __str__(self):
#         return f'Отчет о расхождениях клиентам: "{self.returned_client}" успешно отправлен'
#     # подумать как это реализовать лучше, пока я в замешательстве
#
#
#
# # СДЕЛАТЬ АВТОМАТИЧЕСКУЮ РАССЫЛКУ КЛИЕНТАМ ПРОСТО ИЛИ ТОЛЬКО ПРИ ОПОЗДАНИИ через CELERY
# # или при возврате продукции, но если возврат, то надо отправлять только тому клиенту, у которого возврат
# # думаю сделать флажки опоздания (значит отправка всем клиентам), если возврат, то выбираем одного
# # будем ссылаться на модель клиентов и контакты (почта конкретно) ее вычлинять и будем. Тогда надо будет сделать отдельную
# # переменную в модели клиента, где будет храниться почта или почты, на которую можноо сообщить о возвратной продукции
