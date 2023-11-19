from django.shortcuts import render, redirect, get_object_or_404

from project_app.forms import CreateTaskForm
from project_app.models import Task, FavoriteTask


def index(request):
    task = Task.objects.all()
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
    favorite_task = FavoriteTask.objects.filter(user=request.user)
    context = {
        'favorite_task': [task.task for task in favorite_task]
    }
    return render(request, 'favorite_task.html', context)


def add_to_favorite(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        FavoriteTask.objects.create(user=request.user, task=task)
        return redirect('favorite_task')
    else:
        return redirect('index')