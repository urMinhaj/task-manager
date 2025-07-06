from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task
from .forms import TaskForm
from typing import TypedDict

class TaskDict(TypedDict):
    id: int
    title: str
    description: str
    due_date: str | None

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form, 'error': form.errors})
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        return render(request, 'task_create.html', {'form': form, 'error': form.errors})
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    return Response({'username': request.user.username})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list_api(request):
    tasks = Task.objects.filter(user=request.user)
    data = [TaskDict(id=task.id, title=task.title, description=task.description, due_date=task.due_date) for task in tasks]
    return Response(data)