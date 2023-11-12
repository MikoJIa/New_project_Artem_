from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название задачи')
    descriptions = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    finish_data = models.DateField(verbose_name='Дата окончания', null=True)
    priority_task = models.CharField(verbose_name='Приоритет задачи', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


class FavoriteTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.task} {self.user}'


