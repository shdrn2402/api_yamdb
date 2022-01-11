from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import UsersViewSet


router_v1 = DefaultRouter()

router_v1.register("users", UsersViewSet, basename='users')

app_name = 'api'

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
