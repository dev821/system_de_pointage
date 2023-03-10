# Generated by Django 4.1.5 on 2023-01-30 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_pointage_dateemprunt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointage',
            name='dateEmprunt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date De Emprunt'),
        ),
        migrations.AlterField(
            model_name='pointage',
            name='status',
            field=models.CharField(choices=[('p', 'Present(e)'), ('a', 'Absent(e)')], default='n', help_text="la disponibilté de l'employé(e)", max_length=1, verbose_name='Status'),
        ),
    ]
