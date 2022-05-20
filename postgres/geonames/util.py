
from os import path, makedirs, remove
from datetime import datetime, timedelta

from io import BytesIO
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile

# progress bar
from tqdm import tqdm

from shutil import move
from tempfile import NamedTemporaryFile

CURRENT_DIR = path.dirname( __file__ )
DATA_DIR = path.join( CURRENT_DIR, "data" )
DAY = timedelta( days = 1 )

if not path.isdir( DATA_DIR ):
    makedirs( DATA_DIR )
    print( "Created " + DATA_DIR )

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
            bytes_io = BytesIO( zipresp.read() )
            if bytes_io.getbuffer().nbytes != 0:
                with ZipFile( bytes_io ) as zfile:
                    zfile.extractall( DATA_DIR )
            else:
                print( pretty_file_name + "is a zero length zip file" )
    
    print( pretty_file_name + " is up to date" )
    print( "" )


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urlretrieve(url, filename=output_path, reporthook=t.update_to)

def download( check_file_name, url ):
    p = path.join( DATA_DIR, check_file_name )
    file_exists = path.exists( p )
    
    if not file_exists or get_last_updated_timestamp_diff( p ) > DAY:
        print( "Downloading " + check_file_name )

        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
            try:
                urlretrieve( url, filename = p, reporthook=t.update_to )
            except:
                print( "" )
                print( "Something went wrong when downloading..." )

    print( check_file_name + " is up to date" )
    print( "" )

def pop( file_path ):
    temp_path = None
    with open(file_path, 'r', encoding="utf-8") as f_in:
        with NamedTemporaryFile(mode='w', delete=False) as f_out:
            temp_path = f_out.name
            next(f_in)  # skip first line
            for line in f_in:
                f_out.write(line)

    remove(file_path)
    move(temp_path, file_path)