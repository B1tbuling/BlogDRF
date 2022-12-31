from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


class PostAPIDitail(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostAPIList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostApiCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()


class TagAPIListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


