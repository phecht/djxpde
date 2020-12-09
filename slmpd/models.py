from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count
from django.urls import reverse

# SELECT n.name, c.category, COUNT(*)
#	FROM slmpd_Crime_neighborhood n, slmpd_Crime_category c, slmpd_Crime_reports cr
#	WHERE cr.neighborhood_id = n.id AND cr.category_id = c.id 
#	GROUP BY n.name, c.category
# SELECT n.id, n.name, c.id as catid, c.category, COUNT(*) as crimecounttotal 
#                 FROM slmpd_Crime_neighborhood n, slmpd_Crime_category c, slmpd_Crime_reports cr  
#                 WHERE cr.neighborhood_id = n.id AND cr.category_id = c.id  
#                 GROUP BY n.name, c.id
# 				ORDER BY n.id, c.id
# SELECT cr.id, cr.codedmonth, cr.neighborhood_id, cr.category_id, count(*) as ctotal 
# from slmpd_Crime_reports cr
# GROUP BY cr.neighborhood_id, cr.category_id
# ORDER BY cr.neighborhood_id, cr.category_id
##
# This worked on my machine. Name, Crimes/Name
# cn = Crime_neighborhood.objects.values('name').annotate(cc=Count('Crime_reports'))
# In python manage.py shell
""" 
from django.db.models import Count, Avg, Q
from slmpd.models import Crime_reports, Crime_neighborhood, Crime_category
cn = Crime_neighborhood.crimecounts.all()
 """
 
class Crime_category(models.Model):
    category = models.TextField(max_length=50)

    objects = models.Manager()
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.category


class NeCrimeCountManager(models.Manager):
    ''' Adds the crime count per neighborhood  '''
    def get_queryset(self):
        # Create the queryset  
        qs = super().get_queryset()
        # Annotate queryset with crime counts per neighborhood called cc,
        # then return it
        return qs.annotate(cc=Count("crime_reports")) 

class Crime_neighborhood(models.Model):
    name = models.TextField(max_length=50)
    
    class Meta:
        ordering = ['id']

    objects_crimecounts = NeCrimeCountManager()
    objectsX = models.Manager()
    
    
    
    def __str__(self):
        return self.name


class CrManager(models.Manager):
    ''' crManager overrides base manager to pull related neighbohood and category '''
    def get_queryset(self):
        ''' Run the default get_queryset then add category and neighborhood related records '''
        qs = super().get_queryset()
        return qs.select_related('category','neighborhood')

class Crime_reports(models.Model):
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
    neighborhood = models.ForeignKey(Crime_neighborhood, 
        on_delete=models.CASCADE,
        blank=True)
    category = models.ForeignKey(Crime_category, 
        on_delete=models.CASCADE,
        blank=True)
    

    # This is overriding the default manager. 
    objects = CrManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.crimedesc
