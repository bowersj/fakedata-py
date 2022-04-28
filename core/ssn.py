# 000-00-0000
from numpy.random import default_rng



DIST = default_rng()

def as_number( part_1, part_2, part_3 ):
    return part_1 * 1_000_000 + part_2 * 100_000 + part_3

def as_string_dashes( part_1, part_2, part_3 ):
    return f"{part_1}-{part_2}-{part_3}"

def as_string_no_dashes( part_1, part_2, part_3 ):
    return f"{part_1}{part_2}{part_3}"

def _ssn_part_1():
    val = DIST.integers( low = 1, high = 899 )

    # must account for part 1 can't be 666
    if val != 666:
        return val
    else:
        return _ssn_part_1()




DEFAULT_FORMATTER = as_string_dashes

def ssn( formatter = DEFAULT_FORMATTER ):
    part_1 = _ssn_part_1()
    part_2 = DIST.integers( low = 1, high = 99 )
    part_3 = DIST.integers( low = 1, high = 9999 )

    return formatter( part_1, part_2, part_3 )


print( ssn() )
print( ssn() )
print( ssn() )
print( ssn() )