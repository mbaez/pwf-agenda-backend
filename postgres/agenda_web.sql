--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.4
-- Dumped by pg_dump version 9.5.4

-- Started on 2016-09-15 15:32:11 PYT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';

--
-- TOC entry 2182 (class 1262 OID 38957)
-- Name: agenda_web; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE agenda_web WITH TEMPLATE = template0 ENCODING = 'UTF8';


\connect agenda_web

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';

--
-- TOC entry 1 (class 3079 OID 12435)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2184 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 181 (class 1259 OID 38958)
-- Name: agenda; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE agenda (
    id integer NOT NULL,
    nombre character varying(200),
    apellido character varying(200),
    alias character varying(200),
    telefono integer,
    email character varying(200),
    direccion character varying(300),
    fecha_creacion timestamp without time zone DEFAULT now() NOT NULL,
    fecha_modificacion timestamp without time zone
);


--
-- TOC entry 182 (class 1259 OID 38961)
-- Name: agenda_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE agenda_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2185 (class 0 OID 0)
-- Dependencies: 182
-- Name: agenda_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE agenda_id_seq OWNED BY agenda.id;


--
-- TOC entry 2060 (class 2604 OID 38963)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY agenda ALTER COLUMN id SET DEFAULT nextval('agenda_id_seq'::regclass);


--
-- TOC entry 2063 (class 2606 OID 38971)
-- Name: agenda_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY agenda
    ADD CONSTRAINT agenda_pkey PRIMARY KEY (id);


-- Completed on 2016-09-15 15:32:11 PYT

--
-- PostgreSQL database dump complete
--

