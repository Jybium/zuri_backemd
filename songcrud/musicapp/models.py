from django.db import models

# Create your models here.


class Artiste (models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Song (models.Model):
    artist = models.ForeignKey(
        Artiste, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    date_released = models.DateField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    artiste_id = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Lyrics (models.Model):
    sing = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    song_id = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
