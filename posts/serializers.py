from rest_framework import serializers
from .models import Post, PostImages, Comments, Likes
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comments.objects.create(owner=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        data = validated_data.copy()
        data.pop('publication', None)
        for attr, value, in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class PostImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImages
        fields = ('id', 'image')


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImagesSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True, many=False)
    post_comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ('id', 'owner', 'text', 'date', 'post_images', 'post_comments', 'likes_count')
    
    def create(self, validated_data):
        user = self.context.get('request').user
        publication = Post.objects.create(owner=user, **validated_data)
        images = self.context.get('request').data.getlist('post_images')
        images_list = [PostImages(image=item, publication=publication) for item in images]
        PostImages.objects.bulk_create(images_list)
        return publication

    def update(self, instance, validated_data):
        for attr, value, in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        images = self.context.get('request').data.getlist('post_images')
        if images:
            PostImages.objects.filter(publication=instance).delete()
            images_list = [PostImages(image=item, publication=instance) for item in images]
            PostImages.objects.bulk_create(images_list)
        return instance


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = '__all__'
  
