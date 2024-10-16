from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для модели Group (только для чтения)."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Фильтруем комментарии по post_id из URL."""
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        """Создаём комментарий, добавляя автора и пост."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)

    def update(self, request, *args, **kwargs):
        """Обновление комментария (PUT или PATCH)."""
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Удаление комментария."""
        return super().destroy(request, *args, **kwargs)
