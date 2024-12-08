from rest_framework.viewsets import ModelViewSet
from post.models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Post.objects.filter(book_id=book_id)

    def create(self, request, book_id=None):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(book_id=book_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)