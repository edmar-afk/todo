from django.db import models

# Create your models here.


class Tasks(models.Model):
    task = models.CharField(max_length=250)
    date = models.CharField(max_length=250)