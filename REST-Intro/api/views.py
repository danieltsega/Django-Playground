from rest_framework import generics
from .models import Post
from .serializers import PostSerializers

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers