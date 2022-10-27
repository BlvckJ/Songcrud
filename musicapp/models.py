from django.db import models

# Create your models here

class Artiste(models.Model):

    first_name = models.CharField(max_length=32)

    last_name = models.CharField(max_length=32)

    age = models.DecimalField(max_digits=6, decimal_places = 0)


    def __str__(self):
        return self.first_name



class Song(models.Model):

    title = models.TextField(blank=True)

    date_released = models.DateTimeField(auto_now=True)

    likes = models.IntegerField()

    artiste_id = models.ForeignKey( Artiste, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):

    content = models.TextField(blank=True)

    song_id = models.ForeignKey(Song, on_delete= models.CASCADE)


    def __str__(self):
        return self.song_id.title

