from django.shortcuts import render

from project_app.models import Task


def index(request):
    task = Task.objects.all()
    context = {
        'task': task
    }
    return render(request, 'index.html', context)