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


## Initialization

process: https://github.com/joeblankenship1/Geography_For_Hackers/wiki/Creating-a-GeoNames-Database

You will need to adapt to run in docker, such as downloading the files and then copying them into the docker container.