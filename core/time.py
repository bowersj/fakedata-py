from datetime import time
from math import floor

import numpy as np
from numpy.random import default_rng


sec_in_min = 60
sec_in_hr = 3600
micro_in_sec = 1_000_000
micro_in_min = micro_in_sec * sec_in_min
micro_in_hr  = micro_in_sec * sec_in_hr

default_dist = default_rng()

std  = sec_in_hr * 1

morning_mean = sec_in_hr * 8

afternoon_mean = sec_in_hr * 14

evening_mean = sec_in_hr * 19


def _TOD_helper_utc( mean, std ):
    t = abs( np.random.normal( mean, std ) )
    hrs  = floor( t / sec_in_hr )
    mins = floor( ( t % sec_in_hr ) / sec_in_min )
    secs = floor( t % sec_in_min )
    
    micros = floor( ( t - floor( t ) ) * micro_in_sec )
    
    return time( hrs, mins, secs, micros )


def mornging_utc():
    return _TOD_helper_utc( morning_mean, std )


def afternoon_utc():
    return _TOD_helper_utc( afternoon_mean, std )

def evening_utc():
    return _TOD_helper_utc( evening_mean, std )


def _time_str_to_int( str ):
    t = time( str )
    return t.hour * micro_in_hr + t.minute * micro_in_min + t.second * micro_in_sec + t.microsecond


class BoundedTime_UTC:
    def __init__( self, start, end, generator = default_dist ):
        # TODO: add validation on the format of the stirng
        self.start = _time_str_to_int( start )
        self.end   = _time_str_to_int( end )
        self.rn    = generator

    def gen( self ):
        time_int = self.rn.integers( low = self.start, high = self.end + 1 )
        return time_int
