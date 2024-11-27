from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = router.urls
