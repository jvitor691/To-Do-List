from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'titulo', 'descricao', 'status']
        read_only_fields = ['id']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'status']


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'status']


class StatusPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']
