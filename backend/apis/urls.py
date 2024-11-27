from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 라우터를 생성하지 않고 기본 URL 정보 제공
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'custom_user': request.build_absolute_uri('custom_user/'),
        'book': request.build_absolute_uri('book/'),
        'pots': request.build_absolute_uri('pots/')
    })

urlpatterns = [
    path('', api_root, name='api-root'),  # 기본 엔드포인트
    path('custom_user/', include('apis.custom_user.urls')),
    path('book/', include('apis.book.urls')),
    path('pots/', include('apis.pots.urls')),
]
