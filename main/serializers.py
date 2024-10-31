from rest_framework import serializers
from main.models import Post, Employ


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'created_at', 'uploated_at')
        # fields = "__all__"


class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        fields = '__all__'
