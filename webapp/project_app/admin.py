from django.contrib import admin

from project_app.models import Task, FavoriteTask

admin.site.register(Task)
admin.site.register(FavoriteTask)



