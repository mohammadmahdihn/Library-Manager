from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, BorrowLogSerializer, ReturnSerializer
from .models import BorrowLog, Book
from rest_framework import permissions


# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class BorrowView(CreateAPIView):
    queryset = BorrowLog.objects.all()
    serializer_class = BorrowLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReturnView(UpdateAPIView):
    serializer_class = ReturnSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return BorrowLog.objects.filter(user=self.request.user).filter(is_returned=False)
