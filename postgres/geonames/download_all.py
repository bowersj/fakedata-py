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
        print( "Downloading " + check_file_name )

        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
            urlretrieve( url, filename = p, reporthook=t.update_to )

    print( check_file_name + " is up to date" )
    print( "" )

print( "Starting geonames download" )

try:
    download(
        "readme.txt",
        "https://download.geonames.org/export/dump/readme.txt"
    )


    download_unzip(
        "adminCode5.txt",
        "adminCode5.txt",
        "https://download.geonames.org/export/dump/adminCode5.zip"
    )
    
    download_unzip(
        "allCountries.txt",
        "allCountries.txt",
        "https://download.geonames.org/export/dump/allCountries.zip"
    )

    download_unzip(
        "alternateNames.txt",
        "alternateNames.txt and iso-languagecodes.txt",
        "https://download.geonames.org/export/dump/alternateNames.zip"
    )

    download_unzip(
        "alternateNames.txt",
        "alternateNamesV2.txt and iso-languagecodes.txt",
        "https://download.geonames.org/export/dump/alternateNamesV2.zip"
    )

    download_unzip(
        "cities500.txt",
        "cities500.txt",
        "https://download.geonames.org/export/dump/cities500.zip"
    )

    download_unzip(
        "cities1000.txt",
        "cities1000.txt",
        "https://download.geonames.org/export/dump/cities1000.zip"
    )

    download_unzip(
        "cities5000.txt",
        "cities5000.txt",
        "https://download.geonames.org/export/dump/cities5000.zip"
    )

    download_unzip(
        "cities15000.txt",
        "cities15000.txt",
        "https://download.geonames.org/export/dump/cities15000.zip"
    )



    download_unzip(
        "hierarchy.txt",
        "hierarchy.txt",
        "https://download.geonames.org/export/dump/hierarchy.zip"
    )

    download_unzip(
        "no-country.txt",
        "no-country.txt and readme.txt",
        "https://download.geonames.org/export/dump/no-country.zip"
    )

    download_unzip(
        "shapes_all_low.txt",
        "shapes_all_low.txt",
        "https://download.geonames.org/export/dump/shapes_all_low.zip"
    )

    download_unzip(
        "shapes_simplified_low.txt",
        "shapes_simplified_low.txt",
        "https://download.geonames.org/export/dump/shapes_simplified_low.json.zip"
    )

    download_unzip(
        "userTags.txt",
        "userTags.txt",
        "https://download.geonames.org/export/dump/userTags.zip"
    )



    download(
        "admin1CodesASCII.txt",
        "https://download.geonames.org/export/dump/admin1CodesASCII.txt"
    )

    download(
        "admin2Codes.txt",
        "https://download.geonames.org/export/dump/admin2Codes.txt"
    )

    download(
        "alternateNamesDeletes-2022-05-17.txt",
        "https://download.geonames.org/export/dump/alternateNamesDeletes-2022-05-17.txt"
    )

    download(
        "alternateNamesModifications-2022-05-17.txt",
        "https://download.geonames.org/export/dump/alternateNamesModifications-2022-05-17.txt"
    )

    download(
        "countryInfo.txt",
        "https://download.geonames.org/export/dump/countryInfo.txt"
    )

    download(
        "deletes-2022-05-17.txt",
        "https://download.geonames.org/export/dump/deletes-2022-05-17.txt"
    )

    download(
        "featureCodes_bg.txt",
        "https://download.geonames.org/export/dump/featureCodes_bg.txt"
    )

    download(
        "featureCodes_en.txt",
        "https://download.geonames.org/export/dump/featureCodes_en.txt"
    )

    download(
        "featureCodes_nb.txt",
        "https://download.geonames.org/export/dump/featureCodes_nb.txt"
    )

    download(
        "featureCodes_nn.txt",
        "https://download.geonames.org/export/dump/featureCodes_nn.txt"
    )

    download(
        "featureCodes_no.txt",
        "https://download.geonames.org/export/dump/featureCodes_no.txt"
    )

    download(
        "featureCodes_ru.txt",
        "https://download.geonames.org/export/dump/featureCodes_ru.txt"
    )

    download(
        "featureCodes_sv.txt",
        "https://download.geonames.org/export/dump/featureCodes_sv.txt"
    )

    download(
        "iso-languagecodes.txt",
        "https://download.geonames.org/export/dump/iso-languagecodes.txt"
    )

    download(
        "modifications-2022-05-17.txt",
        "https://download.geonames.org/export/dump/modifications-2022-05-17.txt"
    )

    download(
        "timeZones.txt",
        "https://download.geonames.org/export/dump/timeZones.txt"
    )

except (Exception, Error) as error:
    print( "Error while downloading resources" )
finally:
    print( "finished geonames download" )