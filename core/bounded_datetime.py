from datetime import datetime, timedelta

import pytz
import numpy as np

from random_variable import DISTRIBUTIONS, Random_Integer, get_supported_distribution, assert_distribution
from constants import DEFAULT_DATETIME_PATTERN, DEFAULT_DIST


def _datetime_str_to_int_UTC( str, pattern = DEFAULT_DATETIME_PATTERN ) -> timedelta:
    # TODO: suport an custom pattern
    return datetime.strptime( str, pattern ).toordinal()

class BoundedDatetime_UTC:
    def __init__( self, start, end, pattern = DEFAULT_DATETIME_PATTERN, distribution = DEFAULT_DIST, args = {} ):
        # TODO: add validation on the format of the string
        assert_distribution( distribution )

        dist      = get_supported_distribution( distribution )
        start_int = _datetime_str_to_int_UTC( start, pattern )
        end_int   = _datetime_str_to_int_UTC( end,   pattern )

        if start_int > end_int:
            raise ValueError( "start must be less than end" )

        self.start = start_int
        self.end   = end_int

        self.dist = dist( 
            low  = start_int,
            high = end_int,
            args = args
        )

    def gen( self ):
        return datetime.fromordinal( self.dist.rvs() )

# DO NOT PUT TIMEZONE INFO IN start AND end PARAMETERS, RATHER PASS IN THROUGH THE timezone PARAMETER
class BoundedDatetime_TimeZone:
    def __init__( self, start, end, timezone, pattern = DEFAULT_DATETIME_PATTERN, distribution = DEFAULT_DIST, args = {} ):
        assert_distribution( distribution )
        self.tz    = pytz.timezone( timezone )

        dist  = get_supported_distribution( distribution )

        start_int = _datetime_str_to_int_UTC( start, pattern )
        end_int   = _datetime_str_to_int_UTC( end,   pattern )

        if start_int > end_int:
            raise ValueError( "start must be less than end" )

        self.start = start_int
        self.end   = end_int

        self.dist  = dist( 
            low  = start_int,
            high = end_int,
            args = args
        )

    def gen( self ):
        return datetime.fromordinal( self.dist.rvs() )

# use strftime method on time object to format the string based off of pattern
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

b = BoundedDatetime_UTC( "2000-07-4T07:15:00", "2022-04-28T20:00:00", pattern = "%Y-%m-%dT%H:%M:%S" )
print( b.gen() )


# simple performance testing
# source: https://pymotw.com/3/timeit/#:~:text=The%20timeit()%20method%20returns,one%20item%20in%20the%20dictionary.
# if __name__ == "__main__":
#     import timeit

#    # A few constants
#     range_size = 1000
#     count = 1000
#     setup_statement = ';'.join([
#         "l = [(str(x), x) for x in range(1000)]",
#         "d = {}",
#     ])

#     def show_results( result ):
#         "Print microseconds per pass and per item."
#         global count, range_size
#         per_pass = 1_000_000 * ( result / count )
#         print( '{:6.2f} usec/pass'.format( per_pass ), end=' ' )
#         per_item = per_pass / range_size
#         print( '{:6.2f} usec/item'.format( per_item ) )

#     print("{} items".format( range_size ) )
#     print("{} iterations".format( count ) )
#     print()
#     t = timeit.Timer(
#             'b_time = BoundedDatetime_UTC( "07:15:00", "20:00:00" ); b_time.gen()', 
#             setup = 'from __main__ import BoundedTime_UTC'
#         )
#     show_results( t.timeit( number = count ) )
