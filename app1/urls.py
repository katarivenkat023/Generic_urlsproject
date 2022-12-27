from django.urls import path
from app1.views import *
app1_name='somethong'

urlpatterns=[
    path('first/',first,name='first'),

]