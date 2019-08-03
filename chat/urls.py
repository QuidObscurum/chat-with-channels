from django.urls import path, re_path

from .views import index, room


urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    # re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
