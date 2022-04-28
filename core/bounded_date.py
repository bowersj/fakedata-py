from datetime import date, datetime, timedelta

import pytz
import numpy as np
from random_variable import get_supported_distribution, assert_distribution
from constants import DEFAULT_DATE_PATTERN, DEFAULT_DIST


def _date_str_to_int_UTC( str, pattern = DEFAULT_DATE_PATTERN ) -> timedelta:
    # TODO: suport an custom pattern
    return datetime.strptime( str, pattern ).date().toordinal()

class BoundedDate_UTC:
    def __init__( self, start, end, distribution = DEFAULT_DIST, args = {} ):
        # TODO: add validation on the format of the string
        assert_distribution( distribution )

        dist  = get_supported_distribution( distribution )

        self.start = _date_str_to_int_UTC( start )
        self.end   = _date_str_to_int_UTC( end )

        self.dist  = dist( 
            low  = self.start.days,
            high = self.end.days,
            args = args
        )

    def gen( self ):
        return date.fromordinal( self.dist.rvs() )

# DO NOT PUT TIMEZONE INFO IN start AND end PARAMETERS, RATHER PASS IN THROUGH THE timezone PARAMETER
class BoundedDate_TimeZone:
    def __init__( self, start, end, timezone, distribution = DEFAULT_DIST, args = {} ):
        assert_distribution( distribution )
        self.tz    = pytz.timezone( timezone )

        dist  = get_supported_distribution( distribution )

        self.start = _date_str_to_int_UTC( start )
        self.end   = _date_str_to_int_UTC( end )

        self.dist  = dist( 
            low  = self.start.days,
            high = self.end.days,
            args = args
        )

    def gen( self ):
        return date.fromordinal( self.dist.rvs() )

# use strftime method on time object to format the string based off of pattern
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


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
#             'b_time = BoundedTime_UTC( "07:15:00", "20:00:00" ); b_time.gen()', 
#             setup = 'from __main__ import BoundedTime_UTC'
#         )
#     show_results( t.timeit( number = count ) )
