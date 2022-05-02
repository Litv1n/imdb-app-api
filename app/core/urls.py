from django.urls import path

from .views import MovieListView, DirectorMoviesListView, GenreMoviesListView, ActorDetailView


urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/d=<str:director>/', DirectorMoviesListView.as_view()),
    path('movies/g=<str:genre>/', GenreMoviesListView.as_view()),
    path('actor_stats/<int:id>/', ActorDetailView.as_view()),
]
