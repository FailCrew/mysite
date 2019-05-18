from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
    # add additional fields in here
    name = models.CharField(max_length=20, help_text='Имя')
    lastname = models.CharField(max_length=20, help_text='Фамилия')
    team = models.CharField(max_length=20, help_text='Команда')
    clas = models.CharField(max_length=10, help_text='Класс')
    school = models.CharField(max_length=50, help_text='Школа')
    city = models.CharField(max_length=25, help_text='Город')
    
    def __str__(self):
        return self.email