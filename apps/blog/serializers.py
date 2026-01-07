from rest_framework import serializers
from .models import Post, Category, Tag, Comment


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "excerpt",
            "author",
            "published_at",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "excerpt",
            "content",
            "author",
            "status",
            "published_at",
            "created_at",
        )
