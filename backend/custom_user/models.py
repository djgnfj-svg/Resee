from django.contrib.auth.models import AbstractUser
from django.db import models

# 사용자 (Custom User 모델)
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    verificate = models.IntegerField(default=0)


# 구독 정보 모델
class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="subscription")
    start_date = models.DateField()
    end_date = models.DateField()
    subscription_level = models.CharField(max_length=30)  # 등급
    multi_subscription = models.BooleanField(default=False)  # 다중 구독 여부