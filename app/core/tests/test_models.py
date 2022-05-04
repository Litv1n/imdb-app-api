from django.test import TestCase

from core import models


def sample_actor(first_name='Test first_name', last_name='Test last_name', gender='M'):
    """Create sample actor object"""
    return models.Actor.objects.create(first_name=first_name, last_name=last_name, gender=gender)


def sample_director(first_name='Test first_name', last_name='Test last_name'):
    """Create a sample director object"""
    return models.Director.objects.create(first_name=first_name, last_name=last_name)


def sample_movie(name='Test name', year=1999, rank=9.99):
    """Create a sample movie object"""
    return models.Movie.objects.create(name=name, year=year, rank=rank)


class ModelTests(TestCase):

    def setUp(self):
        self.actor = sample_actor()
        self.director = sample_director()
        self.movie = sample_movie()

    def test_actor_str(self):
        """Test the actor string representation"""
        actor = sample_actor()

        self.assertEqual(str(actor), f'{actor.first_name} {actor.last_name}')

    def test_director_str(self):
        """Test the director string representation"""
        director = sample_director()

        self.assertEqual(
            str(director), f'{director.first_name} {director.last_name}')

    def test_movie_str(self):
        """Test the movie string representation"""
        movie = sample_movie()

        self.assertEqual(str(movie), movie.name)

    def test_director_genre_str(self):
        """Test the DirectorGenre model string representation"""
        director_genre = models.DirectorGenre.objects.create(
            director=self.director,
            genre='Comedy',
            prob=1.11
        )

        self.assertEqual(str(
            director_genre), f'{director_genre.director.first_name}, {director_genre.genre}'
        )

    def test_movie_genre_str(self):
        """Test the MovieGenre model string representation"""
        movie_genre = models.MovieGenre.objects.create(
            movie=self.movie,
            genre='Drama'
        )

        self.assertEqual(str(movie_genre),
                         f'{movie_genre.movie.name}, {movie_genre.genre}'
                         )

    def test_role_str(self):
        """Test Role string representation"""
        role = models.Role.objects.create(
            actor=self.actor,
            movie=self.movie,
            role='Himself'
        )

        self.assertEqual(str(role), role.role)

    def test_movie_director_str(self):
        """Test the MovieDirector model string representation"""
        movie_director = models.MovieDirector.objects.create(
            movie=self.movie,
            director=self.director
        )

        self.assertEqual(str(
            movie_director), f'{movie_director.movie.name}, {movie_director.director.first_name}'
        )
