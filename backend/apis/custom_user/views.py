from rest_framework.viewsets import ModelViewSet
from custom_user.models import CustomUser, Subscription
from .serializers import CustomUserSerializer, SubscriptionSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
