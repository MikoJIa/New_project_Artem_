from django.shortcuts import render, redirect

from project_app.forms import CreateTaskForm
from project_app.models import Task


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


