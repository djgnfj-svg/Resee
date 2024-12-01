"""
URL configuration for Resee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 라우터를 생성하지 않고 기본 URL 정보 제공
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'custom_users': request.build_absolute_uri('custom_users/'),
        'books': request.build_absolute_uri('books/'),  # 'book'에서 'books'로 변경
        'pots': request.build_absolute_uri('pots/')
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    # JWT Token Endpoints
    path('api/', api_root),
    path('api/books/', include('book.urls')),
    path('api/pots/', include('pots.urls')),
    path('api/custom_users/', include('custom_user.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),  # 로그인, 로그아웃 등
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # 회원가입
]

