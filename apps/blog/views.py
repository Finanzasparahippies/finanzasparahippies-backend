from rest_framework import generics
from .models import Post
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
)


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(status="published")


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Post.objects.filter(status="published")
