from django.urls import path
from .views import *


urlpatterns = [

# ---------------READ----------
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('work/', work, name='work'),
]