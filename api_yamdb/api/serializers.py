from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import serializers
from reviews.models import (Category,
                            Comment,
                            Genre,
                            GenreTitle,
                            Review,
                            Title,
                            User)


class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email',)
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username',
            'bio', 'email', 'role',
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')

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


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all())
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        category_object = get_object_or_404(Category, slug=ret['category'])
        ganres_queryset = get_list_or_404(Genre, slug__in=ret['genre'])
        ret['category'] = CategorySerializer(category_object).data
        ret['genre'] = [GenreSerializer(
            genre_object).data for genre_object in ganres_queryset]
        return ret
