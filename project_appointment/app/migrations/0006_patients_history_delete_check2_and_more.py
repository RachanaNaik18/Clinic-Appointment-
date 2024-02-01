# Generated by Django 5.0.1 on 2024-01-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_check2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now=True)),
                ('reason', models.TextField()),
                ('Time', models.TimeField(auto_now=True)),
                ('slot', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='check2',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='appointment_date',
        ),
    ]