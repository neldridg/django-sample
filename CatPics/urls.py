from django.urls import path
from CatPics import views

CatPicsUrlPatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pic-feed', views.pic_feed, name='pic-feed'),
]
