const getSoundex = require( "./soundex.js" );
const utils = require( "../utils.js" );

let tests = {
    "Soundex":     "S532",
    "Example":     "E251",
    "Sownteks":    "S532",
    "Ekzampul":    "E251",
    "Euler":       "E460",
    "Gauss":       "G200",
    "Hilbert":     "H416",
    "Knuth":       "K530",
    "Lloyd":       "L300",
    "Lukasiewicz": "L222",
    "Ellery":      "E460",
    "Ghosh":       "G200",
    "Heilbronn":   "H416",
    "Kant":        "K530",
    "Ladd":        "L300",
    "Lissajous":   "L222",
    "Wheaton":     "W350",
    "Ashcraft":    "A226",
    "Burroughs":   "B622",
    "Burrows":     "B620",
    "O'Hara":      "O600",
    "Washington":  "W252",
    "Wu\t":        "W000",
    "DeSmet":	   "D253",
    "Gutierrez":   "G362",
    "Pfister":     "P236",
    "Jackson":     "J250",
    "Tymczak":     "T522"
};

let soundex = "";
let results = [];
let compare = false;

for (var i in tests){
    if (tests.hasOwnProperty(i)) {
        soundex = getSoundex(i);
        compare = soundex === tests[i];
        results.push( compare );
        console.log(
            i +
            '    \t' +
            tests[i] +
            '\t' +
            soundex +
                '\t' +
            compare
        );
    }
}

console.log( "=======================================" );
console.log( `Tests ${ utils.union( results ) ? "Passed" : "Failed"}` );