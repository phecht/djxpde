# Generated by Django 3.1.3 on 2020-11-29 05:32

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('slmpd', '0002_auto_20201127_1822'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='crime_neighborhood',
            managers=[
                ('objectsX', django.db.models.manager.Manager()),
            ],
        ),
    ]
