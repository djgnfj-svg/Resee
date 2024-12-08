from django.db import models

from book.models import Book
from common.model import TimeStampedModel

# Post 모델
class Post(TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=30)
    script = models.TextField()


# class PostImage(TimeStampedModel):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="posts/images/")