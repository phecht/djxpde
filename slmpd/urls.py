from django.urls import path

from .views import HomePageViewSlmpd, AboutPageViewSlmpd, CrimeReportPageViewSlmpd
from .views import CrimeDetailPageViewSlmpd, NeighborhoodPageViewSlmpd
from .views import NeighborhoodDetailPageViewSlmpd

urlpatterns = [
    # these become slmpd/<path> i.e local:8080/slmpd/about 
    path('', HomePageViewSlmpd.as_view(), name='slmpdhome'),
    path('about/', AboutPageViewSlmpd.as_view(), name='slmpdabout'),
    path('crime/', CrimeReportPageViewSlmpd.as_view(), name='slmpdcrime'), 
    path('crime/detail/<int:pk>/', CrimeDetailPageViewSlmpd.as_view(), name='crime_detail'),    
    path('neighborhood/', NeighborhoodPageViewSlmpd.as_view(), name='slmpdneighborhood'), 
    path('neighborhood/detail/<int:pk>', NeighborhoodDetailPageViewSlmpd.as_view(),
        name='ne-detail'), 

]
