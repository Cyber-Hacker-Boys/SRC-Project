from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendT', views.sendT, name='sendT'),
    path('sendU', views.sendU, name='sendU'),
    path('sendI', views.sendI, name='sendI')
]
