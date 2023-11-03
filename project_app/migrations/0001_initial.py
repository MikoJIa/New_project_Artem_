# Generated by Django 4.2.7 on 2023-11-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('birth_date', models.DateField(verbose_name='Дата рождения автора')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('publication_year', models.IntegerField(max_length=4, verbose_name='Год издания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.author', verbose_name='Имя автора')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.category', verbose_name='Категории')),
            ],
        ),
    ]