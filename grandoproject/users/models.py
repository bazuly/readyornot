from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    job_title = models.CharField(blank=True, null=False, verbose_name='Должность', max_length=128)
