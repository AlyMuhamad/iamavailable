from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:id>/', ChatConsumer.as_asgi())
]