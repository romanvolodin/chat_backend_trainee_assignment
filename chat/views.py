from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat.models import User, Chat, Message
from chat.serializers import UserSerializer, ChatSerializer, MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@api_view(["GET"])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(["POST"])
def list_chats(request):
    try:
        user = User.objects.get(id=request.data["user"])
    except User.DoesNotExist:
        return Response(
            {"error": f"User with id {request.data['user']} not found."}, status=404
        )

    chats = user.chats.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_chat(request):
    serializer = ChatSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"created_chat_id": serializer.data["id"]}, status=201)
