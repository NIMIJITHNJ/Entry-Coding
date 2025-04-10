from django.urls import path
from myApp import views

urlpatterns=[
    path('', views.resume, name='resume')           #To show resume in the home page
]