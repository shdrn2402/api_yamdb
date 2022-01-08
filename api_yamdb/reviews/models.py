from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


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

