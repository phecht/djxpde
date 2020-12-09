from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView 
from .models import Crime_reports, Crime_neighborhood


# Create your views here.
# template_name is relative to the templates folder

class HomePageViewSlmpd(TemplateView):
    template_name = 'slmpd/home.html'


class AboutPageViewSlmpd(TemplateView):
    template_name = 'slmpd/about.html'

# Crime Report views

class CrimeReportPageViewSlmpd(ListView):
    # paginate_by = 10
    template_name = 'slmpd/crimereport.html'
    context_object_name = 'crimereport'
    model = Crime_reports

class CrimeDetailPageViewSlmpd(DetailView):
    template_name = 'slmpd/crimedetail.html'
    context_object_name = 'crimedetail'
    model = Crime_reports

# Neighborhood views

class NeighborhoodPageViewSlmpd(ListView):
    template_name = 'slmpd/neighborhood.html'
    context_object_name = 'neighborhood'
    model = Crime_neighborhood
    
