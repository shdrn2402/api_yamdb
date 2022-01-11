from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from reviews.models import Category, Comment, Genre, Review, Title, User
from api.serializers import (UserSerializer, ReviewSerializer,
                             CommentSerializer, CategorySerializer,
                             GenreSerializer, TitleSerializer)
from api.permisions import IsAuthor, IsModerator, IsAdmin


class UsersViewSet(viewsets.ModelViewSet):
    pass


class TitlesViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(title=title, author=self.request.user)

    def get_permissions(self):
        if self.action == 'partial_update':
            return (IsAuthor(), IsModerator(), IsAdmin(),)
        return super().get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = title.reviews.filter(pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = title.reviews.filter(pk=self.kwargs.get('review_id'))
        serializer.save(title=title, review=review, author=self.request.user)
