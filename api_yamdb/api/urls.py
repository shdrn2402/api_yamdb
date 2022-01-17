from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UsersViewSet
from api.views import get_confirmation_code, get_jwt_token

router_v1 = DefaultRouter()

router_v1.register(r'users', UsersViewSet, basename='users')

app_name = 'api'

v1_auth_patterns = [
    path('signup/', get_confirmation_code),
    path('token/', get_jwt_token)
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(v1_auth_patterns)),
]
