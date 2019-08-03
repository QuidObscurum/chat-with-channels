from django.urls import path, re_path

from .consumers import ChatConsumer


websocket_urlpatterns = [
    # re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
    path('ws/chat/<str:room_name>/', ChatConsumer),
]


# It is good practice to use a common path prefix like /ws/
# to distinguish WebSocket connections from ordinary HTTP connections
# because it will make deploying Channels to a production environment
# in certain configurations easier.
