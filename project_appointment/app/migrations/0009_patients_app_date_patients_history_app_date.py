# Generated by Django 5.0.1 on 2024-01-31 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_patients_slot_alter_timeslots_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='app_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patients_history',
            name='app_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
