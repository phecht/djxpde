from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageViewSlmpd(TemplateView):
    template_name = 'slmpd/home.html'


class AboutPageViewSlmpd(TemplateView):
    template_name = 'slmpd/about.html'

