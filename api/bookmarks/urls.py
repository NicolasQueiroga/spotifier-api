from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('artist', views.ArtistViews, basename='artist')
router.register('album', views.AlbumViews, basename='album')
router.register('playlist', views.PlaylistViews, basename='playlist')
router.register('track', views.TrackViews, basename='track')


urlpatterns = [
    path('bookmark/', include(router.urls))
]
