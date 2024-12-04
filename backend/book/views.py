from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from book.models import Book, BookCategory
from .serializers import BookSerializer, BookCategorySerializer

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        # 현재 요청한 사용자
        user = self.request.user
        # 사용자가 인증된 경우 해당 사용자가 생성한 책만 반환
        if user.is_authenticated:
            return Book.objects.filter(user=user)
        # 인증되지 않은 경우 빈 QuerySet 반환
        return Book.objects.none()

class BookCategoryViewSet(ModelViewSet):
    #TODO : 나중에는 가장많은 갯수를 가진 카테고리를 기본으로 설정
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
