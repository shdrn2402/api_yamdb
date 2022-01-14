from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, GenreViewSet, TitlesViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'genres', GenreViewSet, basename="genres")
router.register(r'titles', TitlesViewSet, basename="titles")

urlpatterns = [
    path(r'v1/', include(router.urls)),
]
