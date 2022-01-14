from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from reviews.models import Category, Comment, Genre, Review, User, Title


from .permisions import IsAdminOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class UsersViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()  # .annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')

    def create(self, request):
        category = get_object_or_404(
            Category, slug=request.data["category"])
        genre = Genre.objects.filter(slug__in=request.data["genre"])
        title = Title.objects.create(name=request.data["name"],
                                     year=request.data["year"],
                                     description=request.data.get(
                                         "description"),
                                     category=category,
                                     )
        title.genre.set(genre)
        return Response(TitleSerializer(title).data)


class CommentViewSet(viewsets.ModelViewSet):
    pass
