from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import Post, Employ
from main.serializers import PostSerializer, EmploySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EmployViewSet(ModelViewSet):
    queryset = Employ.objects.all()
    serializer_class = EmploySerializer
