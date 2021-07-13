from rest_framework import serializers

from posts.models import Post
from posts.serializers import PostImagesSerializer
from users.models import User, Favorite


class PostForUserSerializer(serializers.ModelSerializer):
    post_images = PostImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'date', 'post_images')


class UserSerializer(serializers.ModelSerializer):
    post_owner = PostForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('phone', 'site', 'bio', 'avatar', 'username', 'first_name', 'last_name', 'email', 'post_owner')

