from rest_framework import serializers
from custom_user.models import CustomUser, Subscription

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'start_date', 'end_date', 'subscription_level', 'multi_subscription']
