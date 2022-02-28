from chat import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"chats", views.ChatViewSet)
router.register(r"messages", views.MessageViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
