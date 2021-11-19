from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/ip_forger/', WSConsumer.as_asgi())
]
