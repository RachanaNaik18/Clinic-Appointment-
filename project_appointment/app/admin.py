from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Patients)
class Patient(admin.ModelAdmin):
    list_display =['name', 'age', 'contact', 'reason', 'date', 'Time']

@admin.register(Patients_history)
class Patient(admin.ModelAdmin):
    list_display =['name', 'age', 'contact', 'reason', 'date', 'Time']

admin.site.register(Timeslots)




