from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import serializers
from Resee.settings import DEBUG

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
    
    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            data['user'] = request.user.id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({"detail": "데이터베이스 무결성 오류가 발생했습니다."}, 
                           status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "서버 오류가 발생했습니다."}, 
                           status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            # 현재 사용자와 책의 소유자가 일치하는지 확인
            if instance.user != request.user:
                return Response({"detail": "이 책을 수정할 권한이 없습니다."}, 
                              status=status.HTTP_403_FORBIDDEN)
            
            data = request.data.copy()
            data['user'] = request.user.id
            
            serializer = self.get_serializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "서버 오류가 발생했습니다."}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookCategoryViewSet(ModelViewSet):
    #TODO : 나중에는 가장많은 갯수를 가진 카테고리를 기본으로 설정
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
