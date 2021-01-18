from django.db import models

class Song(models.Model):
    album = models.CharField(default=None, null=True, max_length=100)
    album_link = models.CharField(default=None, null=True, max_length=100)

    song_count = models.CharField(default=None, null=True, max_length=100)

    price = models.CharField(default=None, null=True, max_length=100)

    artist = models.CharField(default=None, null=True, max_length=100)
    artist_link = models.CharField(default=None, null=True, max_length=100)

    category = models.CharField(default=None, null=True, max_length=100)
    category_link = models.CharField(default=None, null=True, max_length=100)

    release_date = models.CharField(default=None, null=True, max_length=100)

    rank = models.IntegerField(default=None, null=True)
    
    image_url = models.CharField(default=None, null=True, max_length=100)

class Date(models.Model):
    timestamp = models.DateTimeField(blank=True)