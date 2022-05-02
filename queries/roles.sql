CREATE TABLE public.roles
(
    actor_id integer NOT NULL,
    movie_id integer NOT NULL,
    role character varying,
    FOREIGN KEY (actor_id) REFERENCES public.actors (id),
    FOREIGN KEY (movie_id) REFERENCES public.movies (id)
);