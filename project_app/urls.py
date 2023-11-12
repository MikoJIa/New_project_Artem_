from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_task/', add_task, name='create_task')
]