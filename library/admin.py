from django.contrib import admin
from .models import Book, BorrowLog


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'is_available')


class BorrowLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'from_date', 'to_date', 'is_returned')


admin.site.register(Book, BookAdmin)
admin.site.register(BorrowLog, BorrowLogAdmin)
