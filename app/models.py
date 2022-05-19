from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Presaved_labs(models.Model):
    number = models.IntegerField()
    author = models.CharField(max_length=30, default = 'Вася')
    group = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now)
    brightness = models.FloatField()
    contrast = models.FloatField()
    roughFocus = models.FloatField()
    preciseFocus = models.FloatField()
    voltage = models.FloatField()
    apertureSize = models.FloatField()
    workDistance = models.FloatField()
    beamCurrent = models.FloatField()
    scale = models.FloatField()


class Saved_labs(models.Model):
    number = models.IntegerField()
    author = models.CharField(max_length=30, default = 'Вася')
    group = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now)
    brightness = models.FloatField()
    contrast = models.FloatField()
    roughFocus = models.FloatField()
    preciseFocus = models.FloatField()
    voltage = models.FloatField()
    apertureSize = models.FloatField()
    workDistance = models.FloatField()
    beamCurrent = models.FloatField()
    scale = models.FloatField()
    score = models.IntegerField(default = 0)


class Lab_description(models.Model):
    number = models.IntegerField()
    deadline = models.CharField(max_length=20)
    task = models.CharField(max_length=300)






