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
    # genre = GenreSerializer(many=True)
    # category = CategorySerializer()
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

    # def to_internal_value(self, data):
    #     genre_queryset = get_list_or_404(Genre, slug__in=data.get('genre'))
    #     category_object = get_object_or_404(
    #         Category, slug=data.get('category'))

    #     data['category'] = CategorySerializer(category_object).data
    #     data['genre'] = [GenreSerializer(
    #         instanse).data for instanse in genre_queryset]
    #     return super(TitleSerializer, self).to_internal_value(data)

    # def create(self, validated_data):
    #     genres = validated_data.pop('genre')
    #     title = Title.objects.create(**validated_data)
    #     for genre in genres:
    #         current_genre, status = Genre.objects.get_or_create(
    #             **genre)
    #         GenreTitle.objects.create(
    #             genre=current_genre, title=title)
    #     return title
