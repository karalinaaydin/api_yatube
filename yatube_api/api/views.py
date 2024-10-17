from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для модели Group (только для чтения)."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)

    def get_post(self):
        """Возвращаем объект поста по параметру post_pk."""
        return get_object_or_404(Post, id=self.kwargs.get('post_pk'))

    def get_queryset(self):
        """Фильтруем комментарии по post_id из URL."""
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """Создаём комментарий, добавляя автора и пост."""
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
