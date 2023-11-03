from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения автора')

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')
    publication_year = models.IntegerField(max_length=4, verbose_name='Год издания')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Имя автора')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категории')

    def __str__(self):
        return self.title
