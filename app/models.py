from django.db import models
from datetime import datetime

# Create your models here.


class Alias(models.Model):
    url = models.CharField(max_length=200)
    alias = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=501)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "aliases"
