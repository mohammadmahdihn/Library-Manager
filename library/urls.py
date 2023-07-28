from django.urls import path
from .views import RegisterView, BorrowView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('borrow/', BorrowView.as_view())
]