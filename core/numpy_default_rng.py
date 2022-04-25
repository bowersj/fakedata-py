from numpy.random import default_rng

class Default_Integer_RNG:
    def __init__( self, low = None, high = None, endpoint = True ) -> None:
        if low < 1:
            raise ValueError( "low must be greater than 0" )

        self.low = low
        self.high = high
        self.endpoint = endpoint
        self.dist = default_rng()
    
    def rvs( self, size ):
        return self.dist.integers( 
            size     = size, 
            low      = self.low, 
            high     = self.high, 
            endpoint = self.endpoint 
        )