from rest_framework import serializers
from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag', 'posts')


class PostListSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True, source='tags.all', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'tags')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', 'tags')

