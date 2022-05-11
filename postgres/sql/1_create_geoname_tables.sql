-- SCHEMA: fake_data

CREATE SCHEMA IF NOT EXISTS fake_data
    AUTHORIZATION admin;

COMMENT ON SCHEMA fake_data
    IS 'filterable source data for fake data generator';

DROP TABLE IF EXISTS fake_data.geoname;
DROP TABLE IF EXISTS fake_data.alternatename;
DROP TABLE IF EXISTS fake_data.countryinfo;
DROP TABLE IF EXISTS fake_data.iso_languagecodes;
DROP TABLE IF EXISTS fake_data.admin2CodesAscii;
DROP TABLE IF EXISTS fake_data.featureCodes;
DROP TABLE IF EXISTS fake_data.timeZones;
DROP TABLE IF EXISTS fake_data.postalcodes;

create table fake_data.geoname (
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

create table fake_data.alternatename (
    alternatenameId INT,
    geonameid INT,
    isoLanguage VARCHAR(7),
    alternateName VARCHAR(200),
    isPreferredName BOOLEAN,
    isShortName BOOLEAN,
    isColloquial BOOLEAN,
    isHistoric BOOLEAN
 );

create table fake_data.countryinfo (
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

CREATE TABLE fake_data.iso_languagecodes(
    iso_639_3 CHAR(4),
    iso_639_2 VARCHAR(50),
    iso_639_1 VARCHAR(50),
    language_name VARCHAR(200)
 );

CREATE TABLE fake_data.admin2CodesAscii (
    code CHAR(80),
    name TEXT,
    nameAscii TEXT,
    geonameid INT
 );

CREATE TABLE fake_data.featureCodes (
    code CHAR(7),
    name VARCHAR(200),
    description TEXT
 );

CREATE TABLE fake_data.timeZones (
    countryCode CHAR(2),
    timeZoneId VARCHAR(200),
    GMT_offset NUMERIC(3,1),
    DST_offset NUMERIC(3,1),
    raw_offset NUMERIC(3,1)
 );

CREATE TABLE fake_data.postalcodes (
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