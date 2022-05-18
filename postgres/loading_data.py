import json
from os import path, system
from datetime import datetime, timedelta

from io import BytesIO
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile

# progress bar
from tqdm import tqdm

import psycopg2
from psycopg2 import Error

CURRENT_DIR = path.dirname( __file__ )
DATA_DIR = path.join( CURRENT_DIR, "data" )
DAY = timedelta( days = 1 )


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def get_last_updated_timestamp_diff( file_path ):
    return datetime.now() - datetime.fromtimestamp( path.getmtime( file_path ) )


# TODO: see link below to add progress support for unzipping
# unzipping: https://stackoverflow.com/questions/4341584/extract-zipfile-using-python-display-progress-percentage
# downloading: https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads#answer-53877507

# credit: https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/
def download_unzip( check_file_name, pretty_file_name, url ):
    p = path.join( DATA_DIR, check_file_name )
    file_exists = path.exists( p )
    
    if not file_exists or get_last_updated_timestamp_diff( p ) > DAY:
        print( "Downloading and unzipping " + pretty_file_name )

        with urlopen( url ) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall( DATA_DIR )
    
    print( pretty_file_name + " is up to date" )


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urlretrieve(url, filename=output_path, reporthook=t.update_to)

def download( check_file_name, url ):
    p = path.join( DATA_DIR, check_file_name )
    file_exists = path.exists( p )
    
    if not file_exists or get_last_updated_timestamp_diff( p ) > DAY:
        print( "Downloading and unzipping " + check_file_name )

        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
            urlretrieve( url, filename = p, reporthook=t.update_to )

    print( check_file_name + " is up to date" )

try:
    # Connect to an existing database
    with open( path.join( CURRENT_DIR, "conn.json" ), 'r' ) as myfile:
        data = myfile.read()
    
    conn = json.loads( data )

    connection = psycopg2.connect( **conn )
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    # print("PostgreSQL server information")
    # print(connection.get_dsn_parameters(), "\n")
    
    # Executing a SQL query
    # print( "Setup Tables" )
    # cursor.execute( open( path.join( CURRENT_DIR, "sql/1_create_geoname_tables.sql" ) ).read() )

    # download the data
    download_unzip(
        "allCountries.txt",
        "allCountries.txt",
        "http://download.geonames.org/export/dump/allCountries.zip"
    )

    download_unzip(
        "alternateNames.txt",
        "alternateNames.txt and iso-languagecodes.txt",
        "http://download.geonames.org/export/dump/alternateNames.zip"
    )

    download(
        "countryInfo.txt",
        "http://download.geonames.org/export/dump/countryInfo.txt"
    )

    download(
        "featureCodes_en.txt",
        "http://download.geonames.org/export/dump/featureCodes_en.txt"
    )

    download(
        "iso-languagecodes.txt",
        "http://download.geonames.org/export/dump/iso-languagecodes.txt"
    )

    download(
        "timeZones.txt",
        "http://download.geonames.org/export/dump/timeZones.txt"
    )

    download(
        "admin2Codes.txt",
        "http://download.geonames.org/export/dump/admin2Codes.txt"
    )


    # load data into the container
    
    # system( "docker cp " + path.join( DATA_DIR, "allCountries/allCountries.txt" ) + " postgis:/opt/data" )
    # system( "docker cp " + path.join( DATA_DIR, "alternateNames/alternateNames.txt" ) + " postgis:/opt/data" )
    # system( "docker cp " + path.join( DATA_DIR, "alternateNames/alternateNames.txt" ) + " postgis:/opt/data" )
    # system( "docker cp " + path.join( DATA_DIR, "alternateNames/iso-languagecodes.txt" ) + " postgis:/opt/data" )
    # copy data into postgres
    # print( "Loading data from container into Postgres" )
    # cursor.execute( open( path.join( CURRENT_DIR, "sql/2_load.sql" ) ).read() )
    # setup columns and indexes
    # print( "creating geospatial columns and indexes (may take a bit)" )
    # cursor.execute( open( path.join( CURRENT_DIR, "sql/3_setupPointColsIndexes.sql" ) ).read() )
    # clean up for efficiency
    # print( "cleaning up records and updating stats" )
    # cursor.execute( "VACUUM FULL ANALYZE" )

    # Fetch result
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")