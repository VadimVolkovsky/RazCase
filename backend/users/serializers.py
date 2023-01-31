from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import City, Profession, Skill, User


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "name")


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("id", "name")


class CustomUserSerializer(UserSerializer):
    """Сериализатор просмотра профиля пользователя"""

    class Meta:
        model = User
        fields = (
            'id', 'name', 'username', 'birthdate', 'gender',
            'city', 'email', 'phone', 'about', 'profession',
            'skills', 'vk_url', 'facebook_url', 'twitter_url',
        )


class CustomUserCreateSerializer(UserCreateSerializer):
    """ Сериализатор создания пользователя """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'name', 'username', 'birthdate', 'gender',
            'city', 'email', 'phone', 'about', 'profession',
            'skills', 'vk_url', 'facebook_url', 'twitter_url',
            'password',
        )