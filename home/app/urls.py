from django.urls import path
from .views import *

urlpatterns = [
    path('',login, name='login'),
    path('registration/', registration, name='registration'),
    path('home/', home, name='home'),
    path('logout', logout, name='logout')
]