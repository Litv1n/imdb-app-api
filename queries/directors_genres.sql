CREATE TABLE public.directors_genres
(
    director_id integer NOT NULL,
    genre character varying(100) NOT NULL,
    prob numeric NOT NULL,
    FOREIGN KEY (director_id) REFERENCES public.directors (id)
);