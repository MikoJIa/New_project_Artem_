from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Exams(models.Model):
    title = models.CharField(max_length=100, verbose_name='Экзамен')
    exam_date = models.DateField(verbose_name='Дата экзамена')
    exam_points = models.IntegerField(verbose_name='Оценка', validators=[MinValueValidator(1),
                                                                         MaxValueValidator(100)])
    teachers = models.ManyToManyField('Teachers', verbose_name='Учителя')
    students = models.ForeignKey('Students', verbose_name='Студенты', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Teachers(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    Available_hourse = models.CharField(max_length=150, verbose_name='Дата экзамена')
    subjects = models.ForeignKey('Subjects', verbose_name='Предметы', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Students(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя студента')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия студента')
    favorite_subjects = models.ForeignKey('Subjects', verbose_name='Любимые предметы',
                                          on_delete=models.CASCADE)
    course = models.IntegerField(verbose_name='Курс')

    def __str__(self):
        return self.last_name


class Subjects(models.Model):
    subject_name = models.CharField(max_length=50, verbose_name='Предмет')

    def __str__(self):
        return self.subject_name
