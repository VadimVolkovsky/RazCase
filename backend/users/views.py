from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import City, Follow, Profession, Skill, User
from users.serializers import (CitySerializer, CustomUserCreateSerializer,
                               CustomUserSerializer, ProfessionSerializer,
                               SkillSerializer, SubscribeSerializer)


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return CustomUserCreateSerializer
        return CustomUserSerializer

    @action(detail=True, methods=['post', 'delete'],
            permission_classes=[IsAuthenticated])
    def subscribe(self, request, **kwargs):
        """Метод для подписки/отписки на пользователей"""
        user = get_object_or_404(User, username=request.user)
        author = get_object_or_404(User, id=self.kwargs.get('id'))

        if request.method == 'POST':
            serializer = SubscribeSerializer(
                author, data=request.data, context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            Follow.objects.create(user=user, author=author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            subscription = get_object_or_404(
                Follow, user=user, author=author
            )
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        """Метод для просмотра своих подписок"""
        user = request.user
        queryset = User.objects.filter(following__user=user)
        pages = queryset  # self.paginate_queryset(queryset) Включить когда будет пагинация
        serializer = SubscribeSerializer(
            pages, many=True, context={'request': request}
        )
        return Response(serializer.data)  # self.get_paginated_response(serializer.data) Включить когда будет пагинация


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer