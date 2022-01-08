from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Category, Comment, Genre, Review, Title, User


class UsersViewSet(viewsets.ModelViewSet):
    pass


class TitlesViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass
