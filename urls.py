#urls.py
from django.urls import path
from . import views


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    path('', views.index, name='index'),
    path('play/<str:id>/', views.play, name='play'),


    # only logged user
    ##################################################
    path('add/', views.add, name='add'),
    path('addInfo/', views.addInfo, name='addInfo'),
    ##################################################


    path('blog/', views.blog, name='blog'),
    path('quizz/', views.quizz, name='quizz'),
    path('travel/', views.travel, name='travel'),
    path('about/', views.about, name='about'),


    ]
