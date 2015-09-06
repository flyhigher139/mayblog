from django.http import HttpResponse
# from django.conf import settings

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main import models
from . import serializers


class CategoryListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAdminUser,)

class TagListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (IsAdminUser,)

class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAdminUser,)