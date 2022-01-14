from django.db.models.fields import SlugField
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Category, Comment, Genre, Review, User, Title


class UserSerializer(serializers.ModelSerializer):
    pass


class ReviewSerializer(serializers.ModelSerializer):
    pass


class CommentSerializer(serializers.ModelSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    #rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year',  # 'rating',
                  'description', 'genre', 'category')
