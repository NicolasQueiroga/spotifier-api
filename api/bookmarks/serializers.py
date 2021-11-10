from rest_framework import serializers
from .models import *


class BookmarksSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Bookmark
        fields = '__all__'
