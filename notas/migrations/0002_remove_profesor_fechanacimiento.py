# Generated by Django 5.0.1 on 2024-01-16 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='FechaNacimiento',
        ),
    ]
