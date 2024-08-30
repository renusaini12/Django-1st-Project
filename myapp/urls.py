from django.urls import path
from .import views

urlpatterns = [
     path('',views.index,name='index'),
     path('table',views.table,name='table'),
     path('about',views.about,name='about'),
     path('contact',views.contact,name='contact'),
     path('gallery',views.gallery,name='gallery'),
     path('reservation',views.reservation,name='reservation'),
     path('room',views.room,name='room'),
     path('signUpData',views.signUpData,name='signUpData'),
     path('reservationData',views.reservationData,name='reservationData'),
     path('loginData',views.loginData,name='loginData'),
     path('signUp',views.signUp,name='signUp'),


]
