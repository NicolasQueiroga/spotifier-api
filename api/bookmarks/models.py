from django.db import models
from authapp.models import User
import datetime


class Bookmark(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    createdAt = models.DateField(
        default=datetime.date.today,
        editable=False
    )
    artist = models.CharField(max_length=200, null=True)
    album = models.CharField(max_length=200, null=True)
    playlist = models.CharField(max_length=200, null=True)
    track = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user}'
