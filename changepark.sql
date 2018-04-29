--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cp_history; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cp_history (
    id integer NOT NULL,
    user_id integer NOT NULL,
    from_curr character varying(255) NOT NULL,
    to_curr character varying(255) NOT NULL,
    amount character varying(255) NOT NULL,
    address_in character varying(255) NOT NULL,
    address_out character varying(255) NOT NULL,
    extraid character varying(255),
    transaction_id character varying(255) NOT NULL,
    exchange_status character varying(255) NOT NULL,
    sync smallint DEFAULT '0'::smallint NOT NULL,
    created_at timestamp(6) without time zone DEFAULT ('now'::text)::timestamp(6) with time zone NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT ('now'::text)::timestamp(6) with time zone NOT NULL
);


ALTER TABLE public.cp_history OWNER TO postgres;

--
-- Name: cp_history_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cp_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cp_history_id_seq OWNER TO postgres;

--
-- Name: cp_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cp_history_id_seq OWNED BY public.cp_history.id;


--
-- Name: cp_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cp_users (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    enabled integer NOT NULL,
    created_at timestamp(6) without time zone DEFAULT ('now'::text)::timestamp(6) with time zone NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT ('now'::text)::timestamp(6) with time zone NOT NULL
);


ALTER TABLE public.cp_users OWNER TO postgres;

--
-- Name: cp_users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cp_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cp_users_id_seq OWNER TO postgres;

--
-- Name: cp_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cp_users_id_seq OWNED BY public.cp_users.id;


--
-- Name: migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.migrations (
    migration character varying(255) NOT NULL,
    batch integer NOT NULL
);


ALTER TABLE public.migrations OWNER TO postgres;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cp_history ALTER COLUMN id SET DEFAULT nextval('public.cp_history_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cp_users ALTER COLUMN id SET DEFAULT nextval('public.cp_users_id_seq'::regclass);


--
-- Data for Name: cp_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cp_history (id, user_id, from_curr, to_curr, amount, address_in, address_out, extraid, transaction_id, exchange_status, sync, created_at, updated_at) FROM stdin;
1	1	btc	ltc	0	3HFoKuvtgG3vhVWfFGsRH7KVnFyhK3dzNi	LhNXzB2AWQ1Q2ArLPwefvrwY9cCENtDz47	\N	e7ff08db497a	new	0	2018-03-03 07:37:57.297075	2018-03-03 07:37:57.297075
\.


--
-- Name: cp_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cp_history_id_seq', 1, true);


--
-- Data for Name: cp_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cp_users (id, username, password, enabled, created_at, updated_at) FROM stdin;
\.


--
-- Name: cp_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cp_users_id_seq', 1, false);


--
-- Data for Name: migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.migrations (migration, batch) FROM stdin;
2018_01_22_181616_create_user_table	1
2018_01_22_181904_create_history_table	1
\.


--
-- Name: cp_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cp_history
    ADD CONSTRAINT cp_history_pkey PRIMARY KEY (id);


--
-- Name: cp_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cp_users
    ADD CONSTRAINT cp_users_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

