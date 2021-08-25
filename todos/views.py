from django.http import request
from rest_framework import generics, permissions
from todos.serializers import TodoSerializer
from todos.models import Todo
from authentication.jwt import JWTAuthentication


class CreateTodoAPIView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListTodoAPIView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
