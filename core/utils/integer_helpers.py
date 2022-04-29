import math

def get_digits( integer ):
    return [ ( integer // ( 10 ** i ) ) % 10  for i in range( math.ceil( math.log( integer, 10 ) ) - 1, -1, -1 ) ]