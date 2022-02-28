from chat import views
from django.urls import path


urlpatterns = [
    path("users/add", views.create_user),
    path("chats/get", views.list_chats),
    path("chats/add", views.create_chat),
    path("messages/get", views.list_messages),
    path("messages/add", views.add_message),
]
