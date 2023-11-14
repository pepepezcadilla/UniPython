from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor)
