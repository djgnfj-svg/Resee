from django.urls import path, include

urlpatterns = [
    path('custom_user/', include('apis.custom_user.urls')),
    path('book/', include('apis.book.urls')),
    path('pots/', include('apis.pots.urls')),
]
