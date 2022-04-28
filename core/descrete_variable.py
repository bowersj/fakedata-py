import numpy as np

import utils.type_validation as utils
from constants import DEFAULT_BATCH_SIZE

class Discrete_Distribution:
    def __init__( self, name, values, percentages, batch_size = DEFAULT_BATCH_SIZE ) -> None:
        if not utils.is_str( name ):
            raise ValueError( "name must be a string" )
        
        if not ( utils.is_arr( values ) and utils.is_arr( percentages ) ):
            raise ValueError( "values and percentages must be a list or an np.array" )

        if len( values ) != len( percentages ):
            raise ValueError( "The number of items in the values and percentages lists must be the same." )

        self.v = values
        self.p = percentages
        self.bs = batch_size
        self.index = -1
        self._RVS = np.array([])

        self._rvs()
        
    
    def _rvs( self ) -> None:
        self.index = -1
        self._RVS = np.random.choice( self.v, self.bs, p = self.p )
    
    def rvs( self, size = 1 ):
        if self.index >= len( self._RVS ) - 1:
            self._rvs()

        self.index = self.index + 1
        idx = self.index

        return self._RVS[ idx : idx + size ]

    

# test = Discrete_Distribution( "test", [ "1", "2", "3" ], [ 0.3, 0.3, 0.4 ] )

# for i in range(1010):
#     val = test.rvs()

#     if (i == 999) or (i == 1000):
#         print( val )
        

# broken
# class Random_Int_From_continuos:
#     def __init__( self, min, max, dist ):
#         if not isinstance( min, int ):
#             raise ValueError( "min must be an integer" )

#         self.dist = dist
#         self.min  = min
#         self.max  = max
#         self.diff = max - min
    
#     def rvs( self, args = None ):
#         return math.floor( self.dist.rvs( **args ) * self.diff ) + self.min
#         # return math.floor( ( self.dist.rvs( **args ) * self.diff ) ) + self.min


# test = Random_Int_From_continuos( min = 1, max = 10, dist = stats.norm )
# args = dict({ "n": 12, "p": 0.6 })
# print( test.rvs( {} ) )

# def _gen_random_int_from_continuos( distribution, min, max, *args ):
#     return math.floor( ( distribution * ( max - min ) ) + min )

# class Generate_Random_Int:
#     def __init__( self, continuos, distribution ):
#         self.D = distribution
#         if continuos:

