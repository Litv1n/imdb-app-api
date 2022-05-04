from django.db import models

from .managers import DirectorManager, GenreManager


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DirectorGenre(models.Model):
    director = models.ForeignKey(Director, models.CASCADE)
    genre = models.CharField(max_length=100)
    prob = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f'{self.director.first_name}, {self.genre}'


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    rank = models.DecimalField(max_digits=10, decimal_places=4,
                               blank=True, null=True)

    objects = models.Manager()
    d_movies = DirectorManager()
    g_movies = GenreManager()

    def __str__(self):
        return self.name


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.movie.name}, {self.genre}'


class Role(models.Model):
    actor = models.ForeignKey(Actor, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE)
    role = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.role


class MovieDirector(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE)
    director = models.ForeignKey(Director, models.CASCADE)

    def __str__(self):
        return f'{self.movie.name}, {self.director.first_name}'
