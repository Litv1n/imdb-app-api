from rest_framework import generics

from .models import Movie, Actor
from .serializers import ActorSerializer, MovieSerializer
from .pagination import MoviesPagination


class BaseMovieAttr(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = MoviesPagination


class MovieListView(BaseMovieAttr):
    """List all movies"""

    def get_queryset(self):
        return Movie.objects.select_related().all().order_by('name')


class DirectorMoviesListView(BaseMovieAttr):
    """List all movies for the director first name"""
    lookup_url_kwarg = 'd'

    def get_queryset(self):
        """Return objects for the director"""
        d_name = self.kwargs['director']
        return Movie.d_movies.get_director_m(d_name).order_by('name')


class GenreMoviesListView(BaseMovieAttr):
    """List all movies for the genre"""
    lookup_url_kwarg = 'g'

    def get_queryset(self):
        """Return objects for the genre"""
        genre = self.kwargs['genre']
        return Movie.g_movies.get_genre_m(genre).order_by('name')


class ActorDetailView(generics.RetrieveAPIView):
    """Actor information"""
    serializer_class = ActorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        actor_id = self.kwargs['id']
        return Actor.objects.filter(id=actor_id)
