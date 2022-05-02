COPY core_actor(id, first_name, last_name, gender) FROM '/../data/imdb_ijs_actors.csv' CSV HEADER;
COPY core_movie(id, name, year, rank) FROM '/../data/imdb_ijs_movies.csv' CSV HEADER;
COPY core_director(id, first_name, last_name) FROM '/../data/imdb_ijs_directors.csv' CSV HEADER;
COPY core_directorgenre(director_id, genre, prob) FROM '/../data/imdb_ijs_directors_genres.csv' CSV HEADER;
COPY core_moviedirector(director_id, movie_id) FROM '/../data/imdb_ijs_movies_directors.csv' CSV HEADER;
COPY core_moviegenre(movie_id, genre) FROM '/../data/imdb_ijs_movies_genres.csv' CSV HEADER;
COPY core_role(actor_id, movie_id, role) FROM '/../data/imdb_ijs_roles.csv' CSV HEADER;