from django.db import models
from authapp.models import User
import datetime


class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField(
        default=datetime.date.today,
        editable=False
    )
    artist = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.artist}'


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField(
        default=datetime.date.today,
        editable=False
    )
    album = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.album}'


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField(
        default=datetime.date.today,
        editable=False
    )
    playlist = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.playlist}'


class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField(
        default=datetime.date.today,
        editable=False
    )
    track = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.track}'
