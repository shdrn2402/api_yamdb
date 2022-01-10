from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    USER = 1 #Добавляем нумерацию для большего функционала 
    MODERATOR = 2
    ADMIN = 3

    ROLE_CHOICES = (
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin')
    )
    username = models.CharField(max_length=25, unique=True, blank=False, null=False, verbose_name='Псевдоним')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Адрес почты')    
    bio = models.TextField(max_length=500, blank=True, verbose_name='Биография')
    name= models.CharField(max_length=30, null=True, verbose_name='Имя пользователя')
    last_name= models.CharField(max_length=30, null=True, verbose_name ='Фамилия')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, verbose_name='Роль')
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta(): # имя и фамилия не одинаковы
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'last_name', ],
                name='unique_object'
            ),
        ]

    def is_admin(self): # дать права доступа админа, если роль Админ
        return self.is_staff or self.role == self.ROLE_CHOICES.ADMIN

    def is_moderator(self): 
        return self.role == self.ROLE_CHOICES.MODERATOR


class Genre(models.Model):
    pass


class Category(models.Model):
    pass


class Title(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
