import numpy as np


"""
print( is_arr( np.array([ 1,2,3,4,5 ]) ) )
print( is_arr( [ 1,2,3,4,5 ] ) )
print( is_arr( { "hi": "There" } ) )
print( is_arr( "string" ) )
print( is_arr( 1 ) )
print( is_arr( 1.0 ) )
"""

def is_arr( item ):
    return type( item ) == np.ndarray or type( item ) == list

def is_str( item ):
    return type( item ) == str and item != ""
        
