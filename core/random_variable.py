from tarfile import SUPPORTED_TYPES
from xmlrpc.client import boolean
from scipy import stats
import numpy as np
import math  as math

from utils import type_validation as utils
from utils.dictionary_helpers import key_default_value
from constants import DEFAULT_BATCH_SIZE, DEFAULT_MU, DEFAULT_SIGMA, DEFAULT_B

class Random_Integer:
    def __init__( self, dist, lower, upper, args = {}, batch_size = DEFAULT_BATCH_SIZE ) -> None:

        if not isinstance( args, dict ):
            raise ValueError( "args must be a dictionary" )

        if not utils.is_int( lower ):
            raise ValueError( "min must be an integer" )

        if not utils.is_int( upper ):
            raise ValueError( "max must be an integer" )

        if not upper > lower:
            raise ValueError( "upper must be at least one greater than lower" )
        
        if not valid_distribution( dist ):
            raise ValueError( "distribution must be one of the following from the scipy.stats library, uniform, truncexpon, or truncnorm" )


        if isinstance( dist, type( stats.uniform ) ):
            self.dist = dist()
            self.p = []

        elif isinstance( dist, type( stats.truncexpon ) ):
            b = key_default_value( args, "b", DEFAULT_B ) 
            self.dist = dist( b )
            self.p = [ "b" ]

        elif isinstance( dist, type( stats.truncnorm ) ):
            mu    = key_default_value( args, "mu",    DEFAULT_MU )
            sigma = key_default_value( args, "sigma", DEFAULT_SIGMA )
            self.p = [ "mu", "sigma" ]
            
            if not ( sigma >= 0.1 and sigma < 1 ):
                raise ValueError( "sigma must fall in the range 0.1 <= sigma < 1" )
            
            if not ( mu >= 0.1 and mu < 1 ):
                raise ValueError( "mu must fall in the range 0.1 <= mu < 1" )

            self.dist = dist( 
                ( lower - mu ) / sigma,
                ( upper - mu ) / sigma,
                loc = mu,
                scale = sigma
            )


        self.bs = batch_size
        self.min = np.float64( lower )
        self.max = np.float64( upper )
        self.diff = np.float64( upper - lower )
        self.index = -1
        self._RVS = np.array([])

        self._rvs()
        
    
    def _scale( self, num ):
        # accounts for values being less or greater than the min or max respectively.
        # this probably occurs due to rounding error
        return ( math.floor( num * self.diff ) + self.min ) % self.max
        # val = math.floor( num * self.diff ) + self.min
        # if val <= self.max and val >= self.min:
        #     return val
        # elif val <= self.max:
        #     return self.min
        # else:
        #     return self.max

    def _rvs( self ) -> None:
        self.index = -1
        self._RVS = self.dist.rvs( size = self.bs )

        for i in range( len( self._RVS ) ):
            self._RVS[i] = self._scale( self._RVS[i] )
    
    def rvs( self ) -> np.float64:
        if self.index >= len( self._RVS ) - 1:
            self._rvs()

        self.index = self.index + 1
        idx = self.index

        return self._RVS[ idx ]

_DISTS = [
    "uniform",
    stats.uniform,
    "truncexpon",
    stats.truncexpon,
    "truncnorm",
    stats.truncnorm
]

DISTRIBUTIONS = { _DISTS[(i*2)]: _DISTS[(i*2) + 1] for i in range( 0, len( _DISTS ) // 2 ) }
# print( DISTRIBUTIONS )

def supported_distribution( name ) -> boolean:
    if not ( isinstance( name, str ) and name != "" ):
        raise ValueError( "name must be a string" )
    
    return DISTRIBUTIONS.has_key( name )
    
    
def get_supported_distribution( name ):
    if not supported_distribution( name ):
        raise ValueError( f"{name} is not a supported distribution" )
    
    return DISTRIBUTIONS.get( name )

def valid_distribution( dist ) -> boolean:
    return isinstance( dist, ( type( stats.uniform ), type( stats.truncexpon ), type( stats.truncnorm ) ) )

# from scipy.stats import truncexpon
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots(1, 1)
# b = 1

# x = np.linspace(
#     truncexpon.ppf(0.01, b),
#     truncexpon.ppf(0.99, b), 
#     100
# )

# ax.plot(x, truncexpon.pdf(x, b),
#        'r-', lw=5, alpha=0.6, label='truncnorm pdf')

# rv = truncexpon( b )

# ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# r = truncexpon.rvs( b, size=1000000 )

# ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
# plt.show()


# Simple test code

# max = 100

# test = Random_Integer( 
#     distribution = stats.uniform,
#     lower = 0,
#     upper = max
# )
# test = Random_Integer( 
#     distribution = stats.truncnorm,
#     lower = 0,
#     upper = max
# )
# test = Random_Integer( 
#     distribution = stats.truncexpon,
#     lower = 0,
#     upper = max
# )

# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )

# boundary = 10_000_000
# limit = boundary - 1
# i = 0
# bad_value = False

# while not bad_value:
#     val = test.rvs()
#     i += 1

#     if val > max:
#         bad_value = True
#         print( val )
    
#     if i > limit:
#         print( "didn't detect with in the first million" )
#         break