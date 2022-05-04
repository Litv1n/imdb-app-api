from django.urls import path

from .views import MovieListView, DirectorMoviesListView, GenreMoviesListView


app_name = 'movie'

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/d=<str:director>/',
         DirectorMoviesListView.as_view(), name='movies-director'),
    path('movies/g=<str:genre>/', GenreMoviesListView.as_view(), name='movies-genre'),
]
