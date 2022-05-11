from utils.read_file import read_file
from descrete_variable import Discrete_Distribution

from source_data.name import FAMOUS_FIRST_NAME, FAMOUS_LAST_NAME, FAMOUS_PEOPLE, FEMALE_FIRST_NAME, MALE_FIRST_NAME, LAST_NAME

# This will have duplicates
# If no duplicates then follow this patthern
#   gen random int, get value, switch value with last value, remove last item (best performance)
class Names:
    def __init__( self, source ) -> None:
        # TODO: add validation for required source  object properties
        self.name = source.get( "name" )
        self.data_prop = source.get( "data_prop" )
        
        p = source.get( "path" )
        
        percentage_prop = source.get( "perc_prop" )
        data = read_file( p, opts = { "format": "arr_dict" } )

        count = len( data )
        self.count = count

        # already contains its own validation
        if percentage_prop:
            self.dist = Discrete_Distribution(
                name = self.data_prop,
                values = data,
                percentages = [ x.get( percentage_prop ) for x in data ]
            )
        else:
            self.dist = Discrete_Distribution(
                name = self.data_prop,
                values = data,
                percentages = [ 1 / count ] * count
            )

    
    def rvs( self ):
        return self.dist.rvs()[0][ self.data_prop ]

    # a convince method
    def rvs_group( self ):
        return [ x.get( self.data_prop ) for x in self.dist.rvs() ]



# test = Names(
#     source = FAMOUS_FIRST_NAME
# )
# test = Names(
#     source = FAMOUS_PEOPLE
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
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )
# print( test.rvs() )