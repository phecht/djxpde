from django.contrib import admin
from .models import Crime_category, Crime_neighborhood, Crime_reports

# Register your models here.
admin.site.register(Crime_category)
admin.site.register(Crime_neighborhood)
admin.site.register(Crime_reports)