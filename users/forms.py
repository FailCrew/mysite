from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Логин')
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Почта')
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Город')
    school = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Школа')
    clas = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Класс')
    team = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Команда')
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'Фамилия'
        }
    ), label='Фамилия сопровождающего')
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Имя  сопровождающего')
    participants = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Участники')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'city', 'school', 'clas', 'team', 'lastname', 'name', 'participants')
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'city', 'school', 'clas', 'team', 'lastname', 'name', 'participants')

