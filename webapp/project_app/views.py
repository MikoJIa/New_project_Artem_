from django.http import HttpResponseNotFound, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.views.generic import DeleteView

from project_app.forms import CreateTaskForm, RegisterUserForm, AuthUserForm
from project_app.models import Task, FavoriteTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout


def index(request):
    task = Task.task_obj.all()
    context = {
        'task': task
    }
    return render(request, 'index.html', context)


def add_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateTaskForm()
    content = {
        'form': form
    }
    return render(request, 'create_task.html', content)


def favorite_task(request):
    favorite_task = FavoriteTask.fav_objects.filter(user=request.user)
    context = {
        'favorite_task': [task.task for task in favorite_task]
    }
    return render(request, 'favorite_task.html', context)


def add_to_favorite(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        FavoriteTask.fav_objects.create(user=request.user, task=task)
        return redirect('index')
    else:
        return redirect('index')


def task_delete(request, id):
    if request.method == 'POST':
        user = request.user
        task = Task.task_obj.get(id=id)
        favorite_task = FavoriteTask.fav_objects.get(user=user, task=task)
        favorite_task.delete()
        return redirect('favorite_task')
    return HttpResponse('<h1>Not task</h1>')


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!!!')
            return redirect('auth_user')
        else:
            messages.error(request, 'Ошибка регистрации!!!')
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = AuthUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthUserForm()
    context = {
        'form': form
    }
    return render(request, 'auth_user.html', context)


def user_logout(request):
    logout(request)
    return redirect('auth_user')



