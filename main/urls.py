from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('booking/', views.booking, name='booking'),
    path('application/', views.application, name='application'),
   
]

 