import numpy as np

def key_default_value( d, key, dv ):
    val = d.get( key )
    
    if val is not None:
        return val
    else:
        return dv