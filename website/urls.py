from django.contrib import admin
from django.urls import path
from .views import NewsList, NewsDetails 
from . import views

urlpatterns = [
    path('', views.home, name="website-home"),
    path('about', views.about, name="website-about"),
    path('project', views.project, name="website-project"),
    path('service', views.service, name="website-service"),
    path('contact', views.contact, name="website-contact"),
    path('news', views.news, name="website-news"),
    path('news/<int:pk>/',NewsDetails.as_view(), name="news-details"),
]