from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'', CustomUserViewSet, basename='user')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = router.urls
