from rest_framework import serializers
from post.models import Post
from rest_framework.response import Response
from rest_framework import status

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'book', 'title', 'script']
        read_only_fields = ['book']  # book 필드는 읽기 전용으로 설정

    def list(self, request):
        book_id = request.query_params.get('book_id')
        if book_id:
            posts = Post.objects.filter(book_id=book_id)
        else :
            return Response({"detail": "book_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
