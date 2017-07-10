from rest_framework import viewsets, permissions
from ..models.post import Post
from ..permissions import IsOwnerOrReadOnly
from ..serializers import SnippetSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    """
    queryset = Post.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )