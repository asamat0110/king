from django.urls import path
from .views import *


urlpatterns = [


# ---------------REGISTER----------
    path('register/', registerUser, name='register'),



# ---------------LOGIN----------
    path('login/', loginUser, name='login'),

# ---------------LOGOUT----------
    path('logout/', logoutUser, name='logout'),

# ---------------READ----------
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('work/', work, name='work'),
    path('search/', search, name='search')
]