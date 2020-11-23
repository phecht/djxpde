from django.contrib import admin
from .models import crime_category, crime_neighborhood, crime_reports

# Register your models here.
admin.site.register(crime_category)
admin.site.register(crime_neighborhood)
admin.site.register(crime_reports)