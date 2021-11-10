from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('bookmarks', views.BookmarkViews, basename='bookmarks')


urlpatterns = [
    path('', include(router.urls))
]
