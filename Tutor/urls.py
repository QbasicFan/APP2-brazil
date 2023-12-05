#urls.py
from django.urls import path
from . import views


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    path('', views.index, name='index'),
    path('play/<str:id>/', views.play, name='play'),

    path('add/', views.add, name='add'),

    path('addInfo/', views.addInfo, name='addInfo'),



    ]
