CREATE TABLE public.movies
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    name character varying(100) NOT NULL,
    year integer NOT NULL,
    rank numeric,
    PRIMARY KEY (id)
);