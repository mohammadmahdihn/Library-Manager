from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, BorrowLogSerializer
from .models import BorrowLog
from rest_framework import permissions


# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class BorrowView(CreateAPIView):
    queryset = BorrowLog.objects.all()
    serializer_class = BorrowLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
