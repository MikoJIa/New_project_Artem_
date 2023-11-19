from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create-task/', add_task, name='create_task'),
    path('favorite-task/', favorite_task, name='favorite_task'),
    path('add-to-favorite/<int:task_id>/', add_to_favorite, name='add_to_favorite')
]