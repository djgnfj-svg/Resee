from rest_framework import serializers
from pots.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'book', 'title', 'script', 'created_at', 'updated_at', 'last_review_date']

