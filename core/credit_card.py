import json
import os

import numpy as np
from numpy.random import default_rng, choice
from utils.integer_helpers import get_digits

current_path = os.path.dirname(__file__)

config = json.load( open( os.path.abspath( os.path.join( current_path, "credit_card\conf.json" ) ) ) )
# 8 bit 0 - 255
INTEGER_TYPE = np.int8
DIST = default_rng()

# TODO: figure out a way to pass in the distribution rather than hard coding it

# CCV functions

def three_digit_code():
    return DIST.integers( low = 100, high = 999 )

def four_digit_code():
    return DIST.integers( low = 1000, high = 9999 )


# Credit Card Functions

def select( arr ) -> int:
    if len( arr ) > 1:
        i = choice( range( 0, len(arr) ) )
        val = arr[i]

        # account for a range of values
        if isinstance( val, list ):
            return DIST.integers( low = val[0], high = val[1], endpoint = True )
        else:
            return val

    else:
        return arr[0]

def credit_card( conf ):
    patterns = conf[ "patterns" ]
    lengths = conf[ "lengths" ]

    # print( patterns )

    # TODO: implement weights 
    pattern = select( patterns )
    digits = get_digits( pattern )
    l_digits = len( digits )
    l = select( lengths )
    length = l - len( digits )
    # check = length % 2
    check = l % 2

    digit = -1
    d = -1
    sum = 0

    digits = np.concatenate(( 
        np.array( digits, dtype = INTEGER_TYPE ), 
        DIST.integers( 
            low = 1, 
            high = 10, 
            size = length - 1, 
            dtype = INTEGER_TYPE 
        ) 
    ))

    for i in range( 0, len( digits ) ):
        digit = digits[i]

        # this changes depending on weather the number of digits is even or odd
        if i % 2 == check:
            d = digit * 2

            if d > 9:
                d -= 9
                
            sum += d
        else:
            sum += digit

    remainder = sum % 10

    if remainder == 0:
        digits = np.append( digits, INTEGER_TYPE( 0 ) )
    else:
        digits = np.append( digits, INTEGER_TYPE( 10 - remainder ) )
    
    ccv = three_digit_code() if conf[ "code" ][ "size" ] == 3 else four_digit_code()

    return {
        "type": conf[ "type" ],
        "number": digits,
        "code": ccv,
        "code_name": conf[ "code" ][ "name" ]
    }

def simple_formatter( cc_object ):
    number = cc_object.get( "number" )
    return "".join( str(x) for x in  number )

def gap_formatter( cc_object, seperator = " " ):
    t = cc_object.get( "type" )
    gaps = config.get( t ).get( "gaps" )
    number = cc_object.get( "number" )

    return custom_gap_formatter( number, gaps, seperator )


def custom_gap_formatter( number, gaps = [], seperator = " " ):
    # t = cc_object.get( "type" )
    # gaps = config.get( t ).get( "gaps" )
    # number = cc_object.get( "number" )
    l_gaps = len( gaps ) - 1

    gap_index = 0
    formatted_number = ""

    for i in range( 0, len( number ) ):
        formatted_number += str( number[ i ] )

        if i + 1 == gaps[ gap_index ]:

            if gap_index + 1 <= l_gaps:
                gap_index += 1

            formatted_number += seperator
    
    return formatted_number


# print( simple_formatter( credit_card( config.get( "visa" ) ) ) )
# print( gap_formatter( credit_card( config.get( "visa" ) ) ) )

# ccs = [ x for x in config.keys() if x!= "types" ]

# print( ccs )

# for cc in ccs:
#     for i in range( 0, 5 ):
#         print( credit_card( config[ cc ] ) )
#     print( "===================================================================================================" )
