from rest_framework import serializers

from posts.models import Post


class SerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class SerializerUpdatePost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'content', 'main_image', 'is_private')


class SerializerCreatePost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'url', 'title', 'content', 'main_image', 'is_private')