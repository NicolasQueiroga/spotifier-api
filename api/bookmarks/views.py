from django.http.response import Http404
from .models import Bookmark, User
from .serializers import BookmarksSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response


class BookmarkViews(viewsets.ModelViewSet):
    serializer_class = BookmarksSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            queryset = Bookmark.objects.filter(user=(user))
        else:
            queryset = Bookmark.objects.all()
        return queryset
