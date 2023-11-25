from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create-task/', add_task, name='create_task'),
    path('favorite-task/', favorite_task, name='favorite_task'),
    path('favorite-task/add-to-favorite/<int:task_id>/', add_to_favorite, name='add_to_favorite'),
    # path('favorite-task/task_delete/<int:id>/', task_delete, name='task_delete')
    path('task_delete/<int:id>/', task_delete,  name='task_delete')
]