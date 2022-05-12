from rest_framework import generics
from .pagination import MoviesPagination
from .serializers import MovieSerializer
from core.models import Movie


class BaseMovieAttr(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = MoviesPagination


class MovieListView(BaseMovieAttr):
    """List all movies"""
    queryset = Movie.objects.select_related().all()

    def get_queryset(self):
        director = self.request.query_params.get('director')
        genre = self.request.query_params.get('genre')
        queryset = self.queryset
        if director:
            queryset = queryset.filter(
                moviedirector__director__first_name=director
            )
        if genre:
            queryset = queryset.filter(
                moviegenre__genre=genre
            )
        return queryset.order_by('name')


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
