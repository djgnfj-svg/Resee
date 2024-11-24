from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'categories', BookCategoryViewSet, basename='category')

urlpatterns = router.urls
