from django.urls import path

from .views import HomePageViewSlmpd, AboutPageViewSlmpd

urlpatterns = [
    path('', HomePageViewSlmpd.as_view(), name='slmpdhome'),
    path('about/', AboutPageViewSlmpd.as_view(), name='slmpdabout'),
]
