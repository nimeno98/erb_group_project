from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('meal',views.meal,name='meal'),
    path('qa',views.qa,name='qa'),
    path('finapply',views.finapply,name='finapply'),  
    path('fee',views.fee,name='fee'),  
    path('booking/', views.booking, name='booking'),
    path('application/', views.application, name='application'),
   
]

 