# Generated by Django 5.0.1 on 2024-01-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='appointment_date',
            field=models.DateField(null=True),
        ),
    ]
