from django.urls import path
from . import views

#Routing of web pages
urlpatterns = [
    path('',views.home,name='home'),
]