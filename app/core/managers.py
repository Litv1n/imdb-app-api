from django.db import models


class MovieQuerySet(models.QuerySet):
    """Specific search in movie queryset"""

    def get_director_movies(self, director):
        """Get movies for the director"""
        return self.select_related().filter(moviedirector__director__first_name=director)

    def get_genre_movies(self, genre):
        """Get movies for the genre"""
        return self.select_related().filter(moviegenre__genre=genre)


class DirectorManager(models.Manager):
    """Manager for listing director movies objects"""

    def get_queryset(self):
        return MovieQuerySet(self.model, using=self._db)

    def get_director_m(self, d_name):
        return self.get_queryset().get_director_movies(d_name)


class GenreManager(models.Manager):
    """Manager for listing genre movies objects"""

    def get_queryset(self):
        return MovieQuerySet(self.model, using=self._db)

    def get_genre_m(self, genre):
        return self.get_queryset().get_genre_movies(genre)
