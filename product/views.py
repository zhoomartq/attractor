from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from . import serializers
from product.models import Category, Article
from product.serializers import CategoryListSerializer


class PermissionMixin:

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAdminUser, ]
        elif self.action == 'list':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser, ]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

class CategoryListView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ArticleListView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer


