from typing import Dict
from matplotlib.pyplot import switch_backend
from scipy import stats
import numpy as np
import math as math

import utils

def build_discrete_distribution( name, values, percentages ):
    if not utils.is_string( name ):
        raise ValueError( "name must be a string" )

    if not ( utils.is_arr( values ) and utils.is_arr( percentages ) ):
        raise ValueError( "values and percentages must be a list or an np.array" )

    if len( values ) != len( percentages ):
        raise ValueError( "The number of items in the values and percentages lists must be the same." )
    
    return stats.rv_discrete( name, value = ( values, percentages ) )


class Random_Int_From_continuos:
    def __init__( self, min, max, dist ):
        if not isinstance( min, int ):
            raise ValueError( "min must be an integer" )

        self.dist = dist
        self.min  = min
        self.max  = max
        self.diff = max - min
    
    def gen( self, args ):
        return self.dist.rvs( **args ) * self.diff
        # return math.floor( ( self.dist.rvs( **args ) * self.diff ) ) + self.min


test = Random_Int_From_continuos( min = 1, max = 2, dist = stats.binom )
args = dict({ "n": 12, "p": 0.6 })
print( stats.binom.rvs( n = 12, p = 0.6, size = 10 ) )

def _gen_random_int_from_continuos( distribution, min, max, *args ):
    return math.floor( ( distribution * ( max - min ) ) + min )

# class Generate_Random_Int:
#     def __init__( self, continuos, distribution ):
#         self.D = distribution
#         if continuos:

