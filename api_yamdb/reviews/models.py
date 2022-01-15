from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"

    ROLE_CHOICES = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    username = models.CharField(max_length=25, unique=True, blank=False, null=False, verbose_name='Псевдоним')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Адрес почты')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Биография')
    role = models.CharField(choices=ROLE_CHOICES, default=USER, max_length=15, verbose_name='Роль')
    first_name= models.CharField(max_length=30, blank=True, verbose_name='Имя пользователя')
    last_name= models.CharField(max_length=30, blank=True, verbose_name ='Фамилия')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)


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
