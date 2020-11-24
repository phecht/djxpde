from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView 
from .models import crime_reports


# Create your views here.

class HomePageViewSlmpd(TemplateView):
    template_name = 'slmpd/home.html'


class AboutPageViewSlmpd(TemplateView):
    template_name = 'slmpd/about.html'

class CrimeReportPageViewSlmpd(ListView):
    template_name = 'slmpd/crimereport.html'
    context_object_name = 'crimereport'
    model = crime_reports

class CrimeDetailPageViewSlmpd(DetailView):
    template_name = 'slmpd/crimedetail.html'
    context_object_name = 'crimedetail'
    model = crime_reports