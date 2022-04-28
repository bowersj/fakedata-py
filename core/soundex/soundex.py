from re import T
import jellyfish

CODES = {
    "a": '', "e": '', "i": '', "o": '', "u": '',
    "b": "1", "f": "1", "p": "1", "v": "1",
    "c": "2", "g": "2", "j": "2", "k": "2", "q": "2", "s": "2", "x": "2", "z": "2",
    "d": "3", "t": "3",
    "l": "4",
    "m": "5", "n": "5",
    "r": "6"
}



def soundex( s, codes = CODES, fixed_length = T, length = 4 ) -> str:
    ns = s.lower()

    f = ns[0]
    r = (f + '').upper()
    value = codes.get( ns[1] )

    if value is not None and value != codes.get( f ):
        r = r + value

    for i in range( 2, len( ns ) ):
        value = codes.get( ns[i] )

        # if value is not None and ( ( i == 1 and value != codes.get( f ) ) or value != codes.get( ns[ i - 1 ] ) ):
        if value is not None and value != codes.get( ns[ i - 1 ] ):
            r = r + value

    r += '000'

    return r[ :length ] if fixed_length else r


# tests = {
#   "Soundex":     "S532",
#   "Example":     "E251",
#   "Sownteks":    "S532",
#   "Ekzampul":    "E251",
#   "Euler":       "E460",
#   "Gauss":       "G200",
#   "Hilbert":     "H416",
#   "Knuth":       "K530",
#   "Lloyd":       "L300",
#   "Lukasiewicz": "L222",
#   "Ellery":      "E460",
#   "Ghosh":       "G200",
#   "Heilbronn":   "H416",
#   "Kant":        "K530",
#   "Ladd":        "L300",
#   "Lissajous":   "L222",
#   "Wheaton":     "W350",
#   "Ashcraft":    "A226",
#   "Burroughs":   "B622",
#   "Burrows":     "B620",
#   "O'Hara":      "O600"
#   }

# for test in tests.keys():
#     print(
#         str( test ) +
#         '    \t' +
#         tests[test] +
#         '\t' +
#         soundex(test, CODES) +
#         '\t' +
#         str( soundex( test, CODES ) == tests[test] ) +
#         '\t' +
#         jellyfish.soundex( test )
#     )