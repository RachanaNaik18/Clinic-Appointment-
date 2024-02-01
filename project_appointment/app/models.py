from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patients(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    contact = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    app_date = models.CharField(max_length=100, null=True)
    reason = models.TextField()
    Time = models.TimeField(auto_now=True)
    slot=models.CharField(max_length=40, null=True)

class Timeslots(models.Model):
    slots=models.CharField(max_length=40)

class Patients_history(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    contact = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    reason = models.TextField()
    app_date = models.CharField(max_length=100, null=True)
    Time = models.TimeField(auto_now=True)
    slot=models.CharField(max_length=1, null=True)
# class check2(models.Model):
#     date = models.DateField(auto_now=True)
#     slots=models.CharField()

    # date count not more than 4
    # slots has choices
    # get date 
    # for length(i.date)==4
    
