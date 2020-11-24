from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class crime_category(models.Model):
    category = models.TextField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.category

class crime_neighborhood(models.Model):
    name = models.TextField(max_length=50)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class crime_reports(models.Model):
    complaint = models.CharField(max_length=9, default='')
    codedmonth = models.CharField(max_length=7, default='')
    dateoccur = models.CharField(max_length=16, default='')  
    flagcrime = models.CharField(max_length=1, default='')
    flagunfounded = models.TextField(max_length=1, default='')
    flagadmin = models.TextField(max_length=1, default='')
    rcount = models.IntegerField(default=0)
    crimecode = models.CharField(max_length=6, default='')
    district = models.CharField(max_length=3, default='')
    crimedesc = models.TextField(max_length=100, default='')
    leadaddress = models.CharField(max_length=10, default='')
    leadstreet = models.TextField(max_length=100, default='')
    importneighborhood = models.IntegerField(default=0)
    locationname = models.CharField(max_length=100, default='')
    locationcomment = models.CharField(max_length=100, default='')
    cadaddress = models.TextField(max_length=10, default='')
    cadstreet =  models.TextField(max_length=50, default='')
    xcoord = models.FloatField(default=0)
    ycoord = models.FloatField(default=0)
    neighborhood = models.ForeignKey(crime_neighborhood, 
        on_delete=models.CASCADE,
        blank=True)
    category = models.ForeignKey(crime_category, 
        on_delete=models.CASCADE,
        blank=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.crimedesc