CREATE TABLE public.movies_genres
(
    movie_id integer NOT NULL,
    genre character varying(50) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES public.movies (id)
);