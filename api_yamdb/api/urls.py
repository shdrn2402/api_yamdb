from django.urls import include, path
from rest_framework import routers

from .views import (GenreList, GenreDetail, TitlesViewSet,
                    CategoryDetail, CategoryList)

router = routers.DefaultRouter()
router.register(r'titles', TitlesViewSet, basename="titles")

urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/categories/',
         CategoryList.as_view(),
         name='category_list'),
    path(r'v1/categories/<slug:slug>/',
         CategoryDetail.as_view(),
         name='category_detail'),
    path(r'v1/genres/',
         GenreList.as_view(),
         name='genres_list'),
    path(r'v1/genres/<slug:slug>/',
         GenreDetail.as_view(),
         name='genres_detail'),
    path('v1/', include('djoser.urls')),
]
