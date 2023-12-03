from django import forms
from django.contrib.auth.models import User

from project_app.models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Enter email',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'autocomplete': 'off'}))
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'autocomplete': 'off'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].help_text = ''
    #     self.fields['password1'].help_text = ''
    #     self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
                                attrs={'class': 'form-control'}))
