from django.db import models
from common.model import TimeStampedModel
from custom_user.models import CustomUser

# 책 카테고리 모델
class BookCategory(models.Model):
    name = models.CharField(max_length=50)  # 카테고리 이름

# 책 모델
class Book(TimeStampedModel):
    # 책 표지 선택지
    COVER_CHOICES = [
        ('cover1', '/book_covers/cover_white.png'),
        ('cover2', '/book_covers/cover_white.png'),
        ('cover3', '/book_covers/cover_white.png'), 
        ('cover4', '/book_covers/cover_white.png'),
        ('cover5', '/book_covers/cover_white.png'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=20)
    cover = models.CharField(
        max_length=20,
        choices=COVER_CHOICES,
        default=COVER_CHOICES[0]
    )
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True, blank=True)
    simple_explanation = models.CharField(max_length=50)

    def __str__(self):
        return self.title
