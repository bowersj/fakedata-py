from matplotlib.pyplot import switch_backend
from scipy import stats
import numpy as np

import utils

def build_discrete_distribution( name, values, percentages ):
    if not utils.is_string( name ):
        raise ValueError( "name must be a string" )

    if not ( utils.is_arr( values ) and utils.is_arr( percentages ) ):
        raise ValueError( "values and percentages must be a list or an np.array" )

    if len( values ) != len( percentages ):
        raise ValueError( "The number of items in the values and percentages lists must be the same." )
    
    return stats.rv_discrete( name, value = ( values, percentages ) )

