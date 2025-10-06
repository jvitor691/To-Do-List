from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Task
from .serializers import (
    TaskSerializer, 
    TaskCreateSerializer, 
    TaskUpdateSerializer, 
    StatusPatchSerializer
)


@api_view(['GET', 'POST'])
@csrf_exempt
def tasks_list_create(request):
    
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            response_serializer = TaskSerializer(task)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def tasks_detail(request, task_id):
   
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskUpdateSerializer(task, data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            response_serializer = TaskSerializer(task)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
@csrf_exempt
def patch_status(request, task_id):
   
    task = get_object_or_404(Task, id=task_id)
    serializer = StatusPatchSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        task = serializer.save()
        response_serializer = TaskSerializer(task)
        return Response(response_serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
