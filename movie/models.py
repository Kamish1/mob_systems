from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(default=2020)
    imdbID = models.CharField(max_length=10, unique=True)
    poster = models.ImageField()
    rated = models.CharField(max_length=10)
    released = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)
    plot = models.TextField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    awards = models.CharField(max_length=200)
    imdbRating = models.FloatField()
    imdbVotes = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    production = models.CharField(max_length=200)


    def get_absolute_url(self):
        return reverse('detail_movie', kwargs={'slug': self.imdbID})

    def __str__(self):
        return f'{self.title}'



class Collage(models.Model):
    list_obj = models.JSONField(default=dict)
    image = models.ImageField()