from django.core import mail
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, viewsets, mixins, status
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from django.http import HttpResponse

from api_yamdb.settings import EMAIL_HOST_USER
from reviews.models import Category, Comment, Genre, Review, Title, User
from api.serializers import UserSerializer, ConfirmationSerializer, ConfirmationSerializer
from api.permisions import IsAdmin
from api.exceptions import UserValueException, MailValueException

@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_code(request):
    """создает пользователя и отправляет код подверждения"""
    serializer = ConfirmationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            email = serializer.data.get('email')
            username = serializer.data.get('username')
            user = User.objects.create(email=email, username=username)
        except Exception:
            if User.objects.get(username=username):
                raise UserValueException("Пользователь с таким логином уже существует")
            if User.objects.get(email=email):
                raise MailValueException("Данный адрес почты уже используется")
    confirmation_code = default_token_generator.make_token(user)
    mail_subject = 'Подтверждение доступа на api_yamdb'
    message = f'Ваш код подтверждения: {confirmation_code}'
    send_mail(mail_subject, message, EMAIL_HOST_USER,
              [email], fail_silently=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_jwt_token(request):

    pass

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=username')


class TitlesViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass
