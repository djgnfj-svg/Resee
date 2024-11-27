from django.db import models
from custom_user.models import CustomUser
from book.models import Book

# Create your models here.
# Post 모델
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=30)
    script = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    last_review_date = models.DateField()