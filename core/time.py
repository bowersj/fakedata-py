from datetime import datetime, time
from math import floor

import pytz
import numpy as np
from numpy.random import default_rng
from random_variable import get_supported_distribution, assert_distribution
from constants import sec_in_min, sec_in_hr, micro_in_sec, micro_in_min, micro_in_hr, DEFAULT_TIME_PATTERN, DEFAULT_DIST


std  = sec_in_hr * 1

morning_mean   = sec_in_hr * 8
afternoon_mean = sec_in_hr * 14
evening_mean   = sec_in_hr * 19


def _TOD_helper_utc( mean, std ):
    t = abs( np.random.normal( mean, std ) )
    hrs  = floor( t / sec_in_hr )
    mins = floor( ( t % sec_in_hr ) / sec_in_min )
    secs = floor( t % sec_in_min )
    
    micros = floor( ( t - floor( t ) ) * micro_in_sec )
    
    return time( hrs, mins, secs, micros )


def morning_utc():
    return _TOD_helper_utc( morning_mean, std )

def afternoon_utc():
    return _TOD_helper_utc( afternoon_mean, std )

def evening_utc():
    return _TOD_helper_utc( evening_mean, std )


def _time_str_to_int_UTC( str, pattern = DEFAULT_TIME_PATTERN ):
    t = datetime.strptime( str, pattern ).time()
    return t.hour * micro_in_hr + t.minute * micro_in_min + t.second * micro_in_sec + t.microsecond

class BoundedTime_UTC:
    def __init__( self, start, end, distribution = DEFAULT_DIST, args = {} ):
        # TODO: add validation on the format of the string
        self.start = _time_str_to_int_UTC( start )
        self.end   = _time_str_to_int_UTC( end )
        
        # TODO: add validation on the format of the string
        assert_distribution( distribution )

        dist  = get_supported_distribution( distribution )
        self.dist  = dist( 
            low  = self.start.days,
            high = self.end.days,
            args = args
        )

    def gen( self ):
        time_int = self.dist.integers( low = self.start, high = self.end )
        
        return time( 
            time_int // micro_in_hr, 
            ( time_int % micro_in_hr ) // micro_in_min, 
            ( time_int % micro_in_min ) // micro_in_sec, 
            time_int % micro_in_sec
        )

# DO NOT PUT TIMEZONE INFO IN start AND end PARAMETERS, RATHER PASS IN THROUGH THE timezone PARAMETER
class BoundedTime_TimeZone:
    def __init__( self, start, end, timezone, distribution = DEFAULT_DIST, args = {} ):
        self.tz    = pytz.timezone( timezone )
        self.start = _time_str_to_int_UTC( start )
        self.end   = _time_str_to_int_UTC( end )

        # TODO: add validation on the format of the string
        assert_distribution( distribution )

        dist  = get_supported_distribution( distribution )
        self.dist  = dist( 
            low  = self.start.days,
            high = self.end.days,
            args = args
        )

    def gen( self ):
        time_int = self.dist.integers( low = self.start, high = self.end + 1 )
        
        return time( 
            time_int // micro_in_hr, 
            ( time_int % micro_in_hr ) // micro_in_min, 
            ( time_int % micro_in_min ) // micro_in_sec, 
            time_int % micro_in_sec,
            self.tz
        )

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