from rest_framework.viewsets import ModelViewSet
from custom_user.models import CustomUser, Subscription
from .serializers import CustomUserSerializer, SubscriptionSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        """
        사용자 생성 (회원가입)
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save() 호출 시 create 메서드 사용
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     """
    #     사용자 목록 조회 (보호된 API)
    #     """
    #     if not request.user.is_staff:  # 관리자만 조회 가능
    #         return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    #     return super().list(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     """
    #     특정 사용자 정보 조회
    #     """
    #     if request.user.is_staff or request.user.id == int(kwargs['pk']):
    #         return super().retrieve(request, *args, **kwargs)
    #     return Response({"detail": "You do not have permission to view this user."}, status=status.HTTP_403_FORBIDDEN)



class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
