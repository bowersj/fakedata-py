import json
import os

import numpy as np
from numpy.random import default_rng, choice
from utils.integer_helpers import get_digits

current_path = os.path.dirname(__file__)

config = json.load( open( os.path.abspath( os.path.join( current_path, "credit_card\conf.json" ) ) ) )

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
            return int( DIST.integers( low = val[0], high = val[1], endpoint = True ) )
        else:
            return int( val )

    else:
        return int( arr[0] )

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

    digits = np.concatenate(( np.array( digits ), DIST.integers( low = 1, high = 10, size = length - 1 ) ))

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
        digits = np.append( digits, 0 )
    else:
        digits = np.append( digits, 10 - remainder )
    
    ccv = three_digit_code() if conf[ "code" ][ "size" ] == 3 else four_digit_code()

    return {
        "type": conf[ "type" ],
        "number": digits,
        "sum": sum,
        "code": ccv,
        "code_name": conf[ "code" ][ "name" ]
    }



print( credit_card( config.get( "visa" ) ) )
print( credit_card( config.get( "visa" ) ) )

print( credit_card( config.get( "mastercard" ) ) )
print( credit_card( config.get( "mastercard" ) ) )
print( credit_card( config.get( "mastercard" ) ) )
print( credit_card( config.get( "mastercard" ) ) )