from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, BorrowLogSerializer, ReturnSerializer, BookSerializer
from .models import BorrowLog, Book
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class BorrowView(CreateAPIView):
    queryset = BorrowLog.objects.all()
    serializer_class = BorrowLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReturnView(RetrieveUpdateAPIView):
    serializer_class = ReturnSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = BorrowLog.objects.filter(is_returned=False)


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
