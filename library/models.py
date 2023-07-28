from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publish_date = models.DateField(null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ', ' + self.author

class BorrowLog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField()
    is_returned = models.BooleanField(default=False)
