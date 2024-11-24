from rest_framework import serializers
from book.models import Book, BookCategory

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'user', 'title', 'simple_explanation', 'created_at', 'last_reviewed_at']

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['id', 'name']
