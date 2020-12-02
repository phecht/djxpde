from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count
from django.urls import reverse

# SELECT n.name, c.category, COUNT(*)
#	FROM slmpd_crime_neighborhood n, slmpd_crime_category c, slmpd_crime_reports cr
#	WHERE cr.neighborhood_id = n.id AND cr.category_id = c.id 
#	GROUP BY n.name, c.category
# SELECT n.id, n.name, c.id as catid, c.category, COUNT(*) as crimecounttotal 
#                 FROM slmpd_crime_neighborhood n, slmpd_crime_category c, slmpd_crime_reports cr  
#                 WHERE cr.neighborhood_id = n.id AND cr.category_id = c.id  
#                 GROUP BY n.name, c.id
# 				ORDER BY n.id, c.id
##
# This worked on my machine. Name, Crimes/Name
# cn = crime_neighborhood.objects.values('name').annotate(cc=Count('crime_reports'))


class crime_category(models.Model):
    category = models.TextField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.category

class neCrimeCountManager(models.Manager):
    '''  '''
    def get_queryset(self):
        qs = super().get_queryset()

        return qs.annotate(cc=Count("crime_reports")) 

class crime_neighborhood(models.Model):
    name = models.TextField(max_length=50)
    
    class Meta:
        ordering = ['id']

    objectsX = neCrimeCountManager()

    def __str__(self):
        return self.name


class crManager(models.Manager):
    ''' crManager overrides base manager to pull related neighbohood and category '''
    def get_queryset(self):
        ''' Run the default get_queryset then add category and neighborhood related records '''
        qs = super().get_queryset()
        # qs = qs.select_related('category')
        return qs.select_related('category','neighborhood')

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
    
    # This is overriding the default manager. 
    objectsX = crManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.crimedesc
