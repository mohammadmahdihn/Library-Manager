from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import transaction
from .models import Book, BorrowLog
from django.contrib.auth.models import User
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'publisher', 'publish_date', 'is_available']


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowLog
        fields = ['id', 'is_returned']

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.is_returned = validated_data['is_returned']
            instance.save()
            book = instance.book
            book.is_available = validated_data['is_returned']
            book.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class BorrowLogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.filter(is_available=True))
    from_date = serializers.ReadOnlyField()
    is_returned = serializers.ReadOnlyField()

    class Meta:
        model = BorrowLog
        fields = ['id', 'book', 'user', 'from_date', 'to_date', 'is_returned']

    def validate(self, attrs):
        if not attrs['book'].is_available:
            raise serializers.ValidationError({'book': 'This book is unavailable'})
        if datetime.date.today() > attrs['to_date']:
            raise serializers.ValidationError({'to_date': 'to_date is unavailable'})
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            borrow_log = BorrowLog.objects.create(user=self.context.get('request', None).user,
                                                  book=validated_data['book'],
                                                  to_date=validated_data['to_date'])
            book = Book.objects.get(id=validated_data['book'].id)
            book.is_available = False
            book.save()
            return borrow_log

