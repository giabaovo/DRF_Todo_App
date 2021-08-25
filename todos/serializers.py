from django.db.models import fields
from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_completed')
