CREATE TABLE public.movies_directors
(
    director_id integer NOT NULL,
    movie_id integer NOT NULL,
    FOREIGN KEY (director_id) REFERENCES public.directors (id),
    FOREIGN KEY (movie_id) REFERENCES public.movies (id)
);