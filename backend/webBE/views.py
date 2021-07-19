from django.shortcuts import render
from rest_framework import viewsets # vieset import
from .serializer import UserSerializer # 생성한 serializer import
from .models import User # User model import

class UserViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = User.objects.all()
    serializer_class = UserSerializer
