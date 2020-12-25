from rest_framework import generics
from posts.models import Posts
from .serializers import TodoSerializer


class TodoListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = TodoSerializer
