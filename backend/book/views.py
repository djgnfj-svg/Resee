from rest_framework.viewsets import ModelViewSet
from book.models import Book, BookCategory
from .serializers import BookSerializer, BookCategorySerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCategoryViewSet(ModelViewSet):
    #TODO : 나중에는 가장많은 갯수를 가진 카테고리를 기본으로 설정
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
