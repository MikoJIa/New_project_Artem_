from django import forms

from project_app.models import Task
from django.contrib.auth import get_user_model


class CreateTaskForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-select',
                                                             'style': 'width: 30%;'}))

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'style': 'width: 50%;'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'finish_data': forms.DateInput(format=('%m-%d'),
                                           attrs={'class': 'form-control',
                                                  'placeholder': 'Select a date',
                                                  'type': 'date',
                                                  'style': 'width: 30%;'}),
            'priority_task': forms.Select(choices=[('Высокий', 'Высокий'),
                                                   ('Средний', 'Средний'),
                                                   ('Низкий', 'Низкий')],
                                          attrs={'class': 'form-select',
                                                 'style': 'width: 30%;'}),

        }
