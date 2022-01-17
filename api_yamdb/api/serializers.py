from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Comment, Review, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        if self.request.method == 'POST':
            if Review.objects.filter(
                    title=title,
                    author=self.request.user
            ).exists():
                raise serializers.ValidationError(
                    'Можно оставить только один отзыв на произведение')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
