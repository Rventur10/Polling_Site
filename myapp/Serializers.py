from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, Post, Follow

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['profile', 'posts']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password'] 
        extra_kwargs = {
            'password': {'write_only': True} 
        }
        

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['poster', 'question', 'upvote_count', 'downvote_count', 'created_at']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['follower', 'followed']
