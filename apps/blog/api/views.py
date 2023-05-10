from rest_framework import viewsets, status, permissions, generics
from .serializers import PostSerializer, PostGETSerializer, BodySerializer, CommentSerializer
from ..models import Post, Body, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostSerializer
        return PostGETSerializer


class BodyRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer


class CommentListCreate(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/blog/api/{post_id}/comment-list-create/
    queryset = Comment.objects.filter(parent_comment__isnull=True)
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['post_id'] = self.kwargs.get('post_id')
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.kwargs.get('post_id')
        qs = qs.filter(post_id=post_id)
        return qs

















