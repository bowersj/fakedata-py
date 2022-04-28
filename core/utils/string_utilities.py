def number_pad_start_4( num, s = "0" ):
    if num > 99:
        if num > 999:
            return str( num )
        else:
            return s + str( num )
    else:
        if num > 9:
            return 2 * s + str( num )
        else:
            return 3 * s + str( num )

def number_pad_start_3( num, s = "0" ):
    if num > 99:
        return str( num )
    else:
        if num > 9:
            return s + str( num )
        else:
            return 2 * s + str( num )

def number_pad_start_2( num, s = "0" ):
    if num > 9:
        return str( num )
    else:
        return s + str( num )