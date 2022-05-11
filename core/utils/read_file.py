from os.path import splitext

import json
import csv





def read_json_file( loc, opts = {} ):
    with open( loc, 'r' ) as myfile:
        data = myfile.read()
    
    return json.loads( data )

def read_csv_file( loc, opts = {} ):
    
    with open( loc ) as myfile:
        if opts.get( "format" ) == "arr_dict":
            del opts[ "format" ]
            # returns an array of objects where each property coresponds to a column
            reader = csv.DictReader( myfile, **opts )

        else:
            delimiter = opts.get( "delimiter", "," )
            quote     = opts.get( "quote",     '"' )
            # returns an array of rows
            reader = csv.reader( myfile, delimiter = delimiter, quotechar = quote )
        
        res = []
        for row in reader:
            res.append( row )

        return res


# This needs to be below all specific reading functions but before the read_file function
EXT_SWITCH = {
    ".json": read_json_file,
    ".csv": read_csv_file
}


# To use this make sure all the desired options are within the EXT_SWITCH object above
def read_file( loc, opts = {} ):
    fn = EXT_SWITCH.get( splitext( loc )[1] )

    if not fn:
        raise ValueError( f"the path, {loc}, does not contain a valid extension. The supported extensions are {', '.join( EXT_SWITCH.keys() )}" )

    return fn( loc, opts )
    
import os
SOURCE_DIR        = r"D:\fakeData\_fakeData\names\data"
# print( read_file( os.path.join( SOURCE_DIR, r"famousFirstNames.json" ) ) )
print( read_file( os.path.join( SOURCE_DIR, r"FamousPeople.csv" ), opts = { "format": "arr_dict", "fieldnames":[ "name" ] } ) )
# print( read_file( "hi.oops" ) ) )