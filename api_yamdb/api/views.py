from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from reviews.models import Comment, Review, Title
from api.serializers import ReviewSerializer, CommentSerializer
from api.permisions import ReviewCommentPermission


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (ReviewCommentPermission,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(title=title, author=self.request.user)

    def get_permissions(self):
        if self.action == 'update':
            raise MethodNotAllowed('PUT-запросы запрещены')
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (ReviewCommentPermission,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        comments = Comment.objects.filter(title=title, review=review)
        return comments

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(
            title=title, review=review, author=self.request.user
        )
