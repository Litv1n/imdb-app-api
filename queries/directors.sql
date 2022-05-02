CREATE TABLE public.directors
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    PRIMARY KEY (id)
);