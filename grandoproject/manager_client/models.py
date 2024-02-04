from django.db import models


class Tag(models.Model):
    "Модель менеджеров"

    name = models.CharField(max_length=124)
    
    def __str__(self):
        return f'Сотрудник {self.name} добавлен'
    

class Client(models.Model):
    "Модель клиентов/поставщиков"
    
    name = models.CharField(max_length=124, null=False)
    inn = models.IntegerField(null=True)
    contacts = models.TextField(max_length=500)
    # manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f'Данные клиента {self.name} успешно добавлены'

