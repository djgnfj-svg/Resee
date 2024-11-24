from rest_framework.viewsets import ModelViewSet
from book.models import Book, BookCategory
from .serializers import BookSerializer, BookCategorySerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCategoryViewSet(ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
