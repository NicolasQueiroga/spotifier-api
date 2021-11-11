from .models import *
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response


@permission_classes([IsAuthenticated])
class ArtistViews(viewsets.ModelViewSet):
    serializer_class = ArtistsSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            queryset = Artist.objects.filter(user=(user))
        else:
            queryset = Artist.objects.all()
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Artist Bookmark Deleted', status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class AlbumViews(viewsets.ModelViewSet):
    serializer_class = AlbumsSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            queryset = Album.objects.filter(user=(user))
        else:
            queryset = Album.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Album Bookmark Deleted', status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class PlaylistViews(viewsets.ModelViewSet):
    serializer_class = PlaylistsSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            queryset = Playlist.objects.filter(user=(user))
        else:
            queryset = Playlist.objects.all()
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Playlist Bookmark Deleted', status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class TrackViews(viewsets.ModelViewSet):
    serializer_class = TracksSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            queryset = Track.objects.filter(user=(user))
        else:
            queryset = Track.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Track Bookmark Deleted', status=status.HTTP_204_NO_CONTENT)
