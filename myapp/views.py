from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from myapp.api_utilis import get_comparable_items
import os , openai , json



from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Post, Account
from .Serializers import UserSerializer, PostSerializer , AccountSerializer

from .api_utilis import get_comparable_items

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class AccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes =  [AllowAny]


def trigger_task(request):
    try:
        response = get_comparable_items()
        return JsonResponse({"result": response})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)