from rest_framework import generics
from .models import Post
from .serializers import PostSerializers

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDetailRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()  # Changed to retrieve all posts initially
    serializer_class = PostSerializers

    def get_queryset(self):
        # Retrieve the ID from the URL parameter (adjust based on your URL pattern)
        pk = self.kwargs.get('id')  # Replace 'pk' with the actual parameter name
        if pk:
            return self.queryset.filter(pk=pk)  # Filter by ID if provided
        return self.queryset 
    
class PostUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  # Changed to retrieve all posts initially
    serializer_class = PostSerializers

    def get_queryset(self):
        # Retrieve the ID from the URL parameter (adjust based on your URL pattern)
        pk = self.kwargs.get('id')  # Replace 'pk' with the actual parameter name
        if pk:
            return self.queryset.filter(pk=pk)  # Filter by ID if provided
        return self.queryset