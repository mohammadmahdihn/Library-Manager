from django.urls import path
from .views import RegisterView, BorrowView, ReturnView, BookListView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('borrow/', BorrowView.as_view()),
    path('return/<int:pk>', ReturnView.as_view()),
    path('books/', BookListView.as_view())
]