SELECT AddGeometryColumn ('fake_data','geoname','the_geom',4326,'POINT',2);
UPDATE fake_data.geoname SET the_geom = ST_PointFromText('POINT(' || longitude || ' ' || latitude || ')', 4326);
CREATE INDEX idx_geoname_the_geom ON fake_data.geoname USING gist(the_geom);

SELECT AddGeometryColumn ('fake_data','postalcodes','the_geom',4326,'POINT',2);
UPDATE fake_data.postalcodes SET the_geom = ST_PointFromText('POINT(' || longitude || ' ' || latitude || ')', 4326);
CREATE INDEX idx_postalcodes_the_geom ON fake_data.postalcodes USING gist(the_geom);