# Generated by Django 3.1.3 on 2020-11-27 18:22

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('slmpd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crime_category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='crime_neighborhood',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='crime_reports',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelManagers(
            name='crime_reports',
            managers=[
                ('objectsX', django.db.models.manager.Manager()),
            ],
        ),
    ]
