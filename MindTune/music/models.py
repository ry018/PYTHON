from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')  # Upload path inside 'media/songs/'
