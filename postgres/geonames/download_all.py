import sys
import json
from os import path, makedirs
from datetime import datetime, timedelta

from io import BytesIO
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile

# progress bar
from tqdm import tqdm

import psycopg2
from psycopg2 import Error

sys.path.append("..")

from util import pop, download, download_unzip, DATA_DIR


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
    # pop( path.join( DATA_DIR, "allCountries.txt" ) )

    download_unzip(
        "alternateNames.txt",
        "alternateNames.txt and iso-languagecodes.txt",
        "https://download.geonames.org/export/dump/alternateNames.zip"
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
        "shapes_simplified_low.json.txt",
        "shapes_simplified_low.json.txt",
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

    # download(
    #     "alternateNamesDeletes-2022-05-17.txt",
    #     "https://download.geonames.org/export/dump/alternateNamesDeletes-2022-05-17.txt"
    # )

    # pop( path.join( DATA_DIR, "alternateNamesDeletes-2022-05-17.txt" ) )

    # download(
    #     "alternateNamesModifications-2022-05-17.txt",
    #     "https://download.geonames.org/export/dump/alternateNamesModifications-2022-05-17.txt"
    # )

    # pop( path.join( DATA_DIR, "alternateNamesModifications-2022-05-17.txt" ) )

    download(
        "countryInfo.txt",
        "https://download.geonames.org/export/dump/countryInfo.txt"
    )

    # download(
    #     "deletes-2022-05-17.txt",
    #     "https://download.geonames.org/export/dump/deletes-2022-05-17.txt"
    # )

    # pop( path.join( DATA_DIR, "deletes-2022-05-17.txt" ) )

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

    # download(
    #     "modifications-2022-05-17.txt",
    #     "https://download.geonames.org/export/dump/modifications-2022-05-17.txt"
    # )
    # pop( path.join( DATA_DIR, "modifications-2022-05-17.txt" ) )

    download(
        "timeZones.txt",
        "https://download.geonames.org/export/dump/timeZones.txt"
    )

    # TODO: pass in save dir which will handle duplicates
    # download_unzip(
    #     "allPostalCodes.txt",
    #     "allPostalCodes.txt",
    #     "http://download.geonames.org/export/zip/allCountries.zip"
    # )

    print ( "remove the first line manually from all files to be loaded into the database" )

except (Exception, Error) as error:
    print( "Error while downloading resources" )
    if error.message:
        print( error.message )

finally:
    print( "finished geonames download" )
