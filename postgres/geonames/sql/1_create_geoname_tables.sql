-- SCHEMA: fakedata

CREATE SCHEMA IF NOT EXISTS fakedata
    AUTHORIZATION admin;

COMMENT ON SCHEMA fakedata
    IS 'filterable source data for fake data generator';

DROP TABLE IF EXISTS fakedata.geoname;
DROP TABLE IF EXISTS fakedata.alternatename;
DROP TABLE IF EXISTS fakedata.countryinfo;
DROP TABLE IF EXISTS fakedata.iso_languagecodes;
DROP TABLE IF EXISTS fakedata.admin2CodesAscii;
DROP TABLE IF EXISTS fakedata.featureCodes;
DROP TABLE IF EXISTS fakedata.timeZones;
DROP TABLE IF EXISTS fakedata.postalcodes;

create table fakedata.geoname (
    geonameid   INT,
    name VARCHAR(200),
    asciiname VARCHAR(200),
    alternatenames TEXT,
    latitude FLOAT,
    longitude FLOAT,
    fclass CHAR(1),
    fcode VARCHAR(10),
    country VARCHAR(2),
    cc2 VARCHAR(200),
    admin1 VARCHAR(20),
    admin2 VARCHAR(80),
    admin3 VARCHAR(20),
    admin4 VARCHAR(20),
    population BIGINT,
    elevation INT,
    gtopo30 INT,
    timezone VARCHAR(40),
    moddate DATE
 );

create table fakedata.alternatename (
    alternatenameId INT,
    geonameid INT,
    isoLanguage VARCHAR(7),
    alternateName VARCHAR(200),
    isPreferredName BOOLEAN,
    isShortName BOOLEAN,
    isColloquial BOOLEAN,
    isHistoric BOOLEAN
 );

create table fakedata.countryinfo (
    iso_alpha2 CHAR(2),
    iso_alpha3 CHAR(3),
    iso_numeric INT,
    fips_code VARCHAR(3),
    name VARCHAR(200),
    capital VARCHAR(200),
    areainsqkm DOUBLE PRECISION,
    population INT,
    continent VARCHAR(2),
    tld VARCHAR(10),
    currencycode VARCHAR(3),
    currencyname VARCHAR(20),
    phone VARCHAR(20),
    postalcode VARCHAR(100),
    postalcoderegex VARCHAR(200),
    languages VARCHAR(200),
    geonameId INT,
    neighbors VARCHAR(50),
    equivfipscode VARCHAR(3)
 );

CREATE TABLE fakedata.iso_languagecodes(
    iso_639_3 CHAR(4),
    iso_639_2 VARCHAR(50),
    iso_639_1 VARCHAR(50),
    language_name VARCHAR(200)
 );

CREATE TABLE fakedata.admin2CodesAscii (
    code CHAR(80),
    name TEXT,
    nameAscii TEXT,
    geonameid INT
 );

CREATE TABLE fakedata.featureCodes (
    code CHAR(7),
    name VARCHAR(200),
    description TEXT
 );

CREATE TABLE fakedata.timeZones (
    countryCode CHAR(2),
    timeZoneId VARCHAR(200),
    GMT_offset NUMERIC(3,1),
    DST_offset NUMERIC(3,1),
    raw_offset NUMERIC(3,1)
 );

CREATE TABLE fakedata.postalcodes (
    countrycode CHAR(2),
    postalcode  VARCHAR(20),
    placename   VARCHAR(180),
    admin1name  VARCHAR(100),
    admin1code  VARCHAR(20),
    admin2name  VARCHAR(100),
    admin2code  VARCHAR(20),
    admin3name  VARCHAR(100),
    admin3code  VARCHAR(20),
    latitude    FLOAT,
    longitude   FLOAT,
    accuracy    SMALLINT
 );

CREATE TABLE IF NOT EXISTS fakedata.city500
(
    geonameid integer,
    name character varying(200),
    asciiname character varying(200),
    alternatenames text,
    latitude double precision,
    longitude double precision,
    fclass character(1),
    fcode character varying(10),
    country character varying(2),
    cc2 character varying(200),
    admin1 character varying(20),
    admin2 character varying(80),
    admin3 character varying(20),
    admin4 character varying(20),
    population bigint,
    elevation integer,
    gtopo30 integer,
    timezone character varying(40),
    moddate date
);

CREATE TABLE IF NOT EXISTS fakedata.city1000
(
    geonameid integer,
    name character varying(200),
    asciiname character varying(200),
    alternatenames text,
    latitude double precision,
    longitude double precision,
    fclass character(1),
    fcode character varying(10),
    country character varying(2),
    cc2 character varying(200),
    admin1 character varying(20),
    admin2 character varying(80),
    admin3 character varying(20),
    admin4 character varying(20),
    population bigint,
    elevation integer,
    gtopo30 integer,
    timezone character varying(40),
    moddate date
);

CREATE TABLE IF NOT EXISTS fakedata.city5000
(
    geonameid integer,
    name character varying(200),
    asciiname character varying(200),
    alternatenames text,
    latitude double precision,
    longitude double precision,
    fclass character(1),
    fcode character varying(10),
    country character varying(2),
    cc2 character varying(200),
    admin1 character varying(20),
    admin2 character varying(80),
    admin3 character varying(20),
    admin4 character varying(20),
    population bigint,
    elevation integer,
    gtopo30 integer,
    timezone character varying(40),
    moddate date
);

CREATE TABLE IF NOT EXISTS fakedata.city15000
(
    geonameid integer,
    name character varying(200),
    asciiname character varying(200),
    alternatenames text,
    latitude double precision,
    longitude double precision,
    fclass character(1),
    fcode character varying(10),
    country character varying(2),
    cc2 character varying(200),
    admin1 character varying(20),
    admin2 character varying(80),
    admin3 character varying(20),
    admin4 character varying(20),
    population bigint,
    elevation integer,
    gtopo30 integer,
    timezone character varying(40),
    moddate date
);

CREATE TABLE IF NOT EXISTS fakedata.hierarchy
(
    parentid integer,
    childid integer,
    type VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS fakedata.admin1codeascii
(
    code      VARCHAR(20),
    name      TEXT,
    asciiname TEXT,
    geonameid integer
);

CREATE TABLE IF NOT EXISTS fakedata.admin5code
(
    geonameid integer,
    adm5code VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS fakedata.nocountry
(
    geonameid integer,
    name character varying(200),
    asciiname character varying(200),
    alternatenames text,
    latitude double precision,
    longitude double precision,
    fclass character(1),
    fcode character varying(10),
    country character varying(2),
    cc2 character varying(200),
    admin1 character varying(20),
    admin2 character varying(80),
    admin3 character varying(20),
    admin4 character varying(20),
    population bigint,
    elevation integer,
    gtopo30 integer,
    timezone character varying(40),
    moddate date
);