## Setting up postGIS in Docker

1. run the following commands
	`docker volume create pg_data`
	`docker network create --driver bridge pgnetwork`

	`docker run --name=postgis -d -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DBNAME=gis -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v pg_data:/var/lib/postgresql --hostname=POSTGRES --network=pgnetwork --restart=always --shm-size=2g postgis/postgis`
	`docker run --name=pgadmin -p 5050:80  -e "PGADMIN_DEFAULT_EMAIL=name@example.com" -e "PGADMIN_DEFAULT_PASSWORD=admin" --network=pgnetwork -d dpage/pgadmin4`
2. log into pgadmin by going to localhost:5050
3. create a server with the following settings
	server name:		fake_data
	server description:	"Postgres instance for working with source data"
	(switch to connection tab)
	hostname:	POSTGRES
	port:		5432
	user:		admin
	password:	admin



High level walkthrough (most recient) https://github.com/joeblankenship1/Geography_For_Hackers/wiki/Creating-a-GeoNames-Database
Complete walk-through https://event.ifi.uni-heidelberg.de/wp-content/uploads/2017/03/geonames_installation.pdf
Shorter, older version https://medium.com/pixel-heart/howto-dump-geonames-into-postgresql-and-postgis-395fab58f4bc
Code walkthrough, ruby, https://gist.github.com/kaspergrubbe/b0f87329319e6442d676c0edbf635be9
Node example https://stackoverflow.com/questions/51812845/how-to-properly-insert-the-geonames-1-5gib-file-into-postgresql-using-node



## Initialization

process: https://github.com/joeblankenship1/Geography_For_Hackers/wiki/Creating-a-GeoNames-Database

You will need to adapt to run in docker, such as downloading the files and then copying them into the docker container.

GeoNames decoders
http://www.geonames.org/maps/addresses.html#address
http://www.geonames.org/export/reverse-geocoding.html

free node version, will need some work
https://github.com/tomayac/local-reverse-geocoder
https://hub.docker.com/r/mesripour/local-reverse-geocoder


https://www.google.com/search?q=creating+a+reverse+geocoding+with+geonames+docker&rlz=1C1GCEU_enUS961US961&sxsrf=ALiCzsbhj-moV6lKeeejrBJvYpyCtcN9UQ%3A1652673858939&ei=Qs2BYpPlOJSekPIP9f20-AE&ved=0ahUKEwiTjqrykeP3AhUUD0QIHfU-DR8Q4dUDCA4&uact=5&oq=creating+a+reverse+geocoding+with+geonames+docker&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgAToHCCMQsAMQJzoHCAAQRxCwAzoICCEQFhAdEB46BQghEKsCSgQIQRgASgQIRhgAUMcGWNEUYK0XaAFwAXgAgAGNAYgBjgeSAQMwLjeYAQCgAQHIAQnAAQE&sclient=gws-wiz






Consider using pelias to reverse geocode data.

setting up on windows 10, very vauge but should be a good starting point
https://github.com/pelias/docker/issues/124#issuecomment-1121532245
https://github.com/pelias/docker/



list of GIS data sources
https://freegisdata.rtwilson.com/



Everything below is under a coopy left license and can only be used as a reference!!!!!
--------------------------------------------------------------------------------------------------------

## Setting up server for reverse geocoding
https://hub.docker.com/r/mediagis/nominatim/
https://github.com/mediagis/nominatim-docker/tree/master/4.0

## openstreetdata download
https://wiki.openstreetmap.org/wiki/Downloading_data
https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts



### helpful links
https://osm2pgsql.org/

## create map server for off line data
https://medium.com/@rajitha.mail48/create-a-docker-image-of-an-offline-open-street-map-server-9fdedd433cc8




## Possible source of texts
https://archive.org/about/


## more Location data
https://laendercode.net/en/

## postGIS image
https://registry.hub.docker.com/r/postgis/postgis



Command to create a docker container with nominatim running

TODO: make sure to update the postgres settings based off of the recommended settings..
TODO: pipe output to a file

to recreate the container run the same command that created it

username = nominatim

docker run -it -e PBF_PATH=/nominatim/data/north-america-latest.osm.pbf -e FREEZE=true -e IMPORT_WIKIPEDIA=false -e IMPORT_US_POSTCODES=false -e IMPORT_GB_POSTCODES=false -e IMPORT_TIGER_ADDRESS=false -e NOMINATIM_PASSWORD=qaIACxO6wMR3 --shm-size=8g -v F:\nominatim\postgresData:/var/lib/postgresql/12/main -v F:\nominatim\data:/nominatim/data -p 8080:8080 -p 2718:5432 --name=nominatim --hostname=nominatim --network=pgnetwork mediagis/nominatim:4.0

docker network connect nominatim 