from django.urls import path

from .views import HomePageViewSlmpd, AboutPageViewSlmpd, CrimeReportPageViewSlmpd

urlpatterns = [
    path('', HomePageViewSlmpd.as_view(), name='slmpdhome'),
    path('about/', AboutPageViewSlmpd.as_view(), name='slmpdabout'),
    path('crime/', CrimeReportPageViewSlmpd.as_view(), name='slmpdcrime'),    
]
