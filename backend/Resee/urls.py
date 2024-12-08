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
    TokenVerifyView,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 라우터를 생성하지 않고 기본 URL 정보 제공
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'custom_users': request.build_absolute_uri('custom_users/'),
        'books': request.build_absolute_uri('books/'),  # 'book'에서 'books'로 변경
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    # JWT Token Endpoints
    path('api/', api_root),
    path('api/books/', include('book.urls')),
    path('api/books/<int:book_id>/posts/', include('post.urls')),
    path('api/custom_users/', include('custom_user.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

