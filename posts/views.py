from rest_framework import generics
from .models import Post
from .permissions import IsAuthOrReadOnly
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
