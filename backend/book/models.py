from django.db import models
from custom_user.models import CustomUser

# 책 카테고리 모델
class BookCategory(models.Model):
    name = models.CharField(max_length=50)  # 카테고리 이름

# 책 모델
class Book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=20)
    simple_explanation = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    last_reviewed_at = models.DateField()
