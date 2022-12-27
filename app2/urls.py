from django.urls import path
from app2.views import *
app_name='something'

urlpatterns=[
    path('third/',third,name='third'),

]
