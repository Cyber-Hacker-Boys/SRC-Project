from django.urls import path

from . import views

urlpatterns = [
    path('ipApp/', views.index, name='index')
]
