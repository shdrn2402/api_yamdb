from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from reviews.models import Category, Comment, Genre, Review, Title, User

from .permisions import IsAdminOrReadOnly, ReviewCommentPermission
from .serializers import CategorySerializer, GenreSerializer, ReviewSerializer, TitleSerializer


class UsersViewSet(viewsets.ModelViewSet):
    pass


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


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CategoryDetail(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreDetail(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')

    def perform_create(self, serializer):
        category = get_object_or_404(
            Category, slug__in=serializer.validated_data['category'].values())
        serializer.save(
            # name=serializer.validated_data.get('name'),
            # year=serializer.validated_data.get('year'),
            # genre=serializer.validated_data.get('genre'),
            # description=serializer.validated_data.get('description'),
            category=category
        )


class CommentViewSet(viewsets.ModelViewSet):
    pass
