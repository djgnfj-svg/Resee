from rest_framework.routers import DefaultRouter
from .views import PostViewSet, BookImageViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'images', BookImageViewSet, basename='image')

urlpatterns = router.urls
