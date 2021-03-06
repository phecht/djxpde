# Generated by Django 3.1.3 on 2020-11-22 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crime_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='crime_neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='crime_reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(default='', max_length=9)),
                ('codedmonth', models.CharField(default='', max_length=7)),
                ('dateoccur', models.CharField(default='', max_length=16)),
                ('flagcrime', models.CharField(default='', max_length=1)),
                ('flagunfounded', models.TextField(default='', max_length=1)),
                ('flagadmin', models.TextField(default='', max_length=1)),
                ('rcount', models.IntegerField(default=0)),
                ('crimecode', models.CharField(default='', max_length=6)),
                ('district', models.CharField(default='', max_length=3)),
                ('crimedesc', models.TextField(default='', max_length=100)),
                ('leadaddress', models.CharField(default='', max_length=10)),
                ('leadstreet', models.TextField(default='', max_length=100)),
                ('importneighborhood', models.IntegerField(default=0)),
                ('locationname', models.CharField(default='', max_length=100)),
                ('locationcomment', models.CharField(default='', max_length=100)),
                ('cadaddress', models.TextField(default='', max_length=10)),
                ('cadstreet', models.TextField(default='', max_length=50)),
                ('xcoord', models.FloatField(default=0)),
                ('ycoord', models.FloatField(default=0)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='slmpd.crime_category')),
                ('neighborhood', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='slmpd.crime_neighborhood')),
            ],
        ),
    ]
