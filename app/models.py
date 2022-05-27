from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Presaved_labs(models.Model):
    number = models.IntegerField()
    user_id = models.IntegerField()
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
    user_id = models.IntegerField(default = 0)
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
    title = models.CharField(max_length=300, default="заголовок")
    task = models.CharField(max_length=1500)




# class User_Token(models.Model):
#     username = models.CharField(max_length=300)
#     token = models.CharField(max_length=40)






