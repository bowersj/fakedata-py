// credit card test cases
// const tests =[
//     [ 1,2,3,4,5,6,7,8,9,1,2,3 ],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4 ],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6 ],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7 ],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8 ],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9 ],
//     [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,0 ]
// ];

const ccTypes = require( "./ccTypes.js" );
const utils = require( "../utils.js" );


module.exports = { _buildCCFormatter };

/**
 * @param {String} varName - the name of the variable be referenced
 * @param {String} path - the path to an array, it must start with a ".",
 *      unless no path is needed, in which case pass in ""
 * @param {Number|string} index - the index with in an array
 *
 */
function digitToken_simple( varName, path, index ){
    let val = _buildPath( varName, `${path}[${index}]` );
    return `${val}.toString()`;
}


/**
 * @param {String} varName - the name of the variable be referenced
 * @param {String} path - the path to an array, it must start with a ".",
 *      unless no path is needed, in which case pass in ""
 */
function _buildPath( varName, path ){
    return `${varName}${path}`;
}


function _buildArrayFormatterBody( tokens, paramName, map, opts ){

    let functionBody = "return ";
    let token = "";
    // let expression = "";
    let path = "";
    let strToken = "";

    // console.log( tokens );

    let j = 0;
    for( let i = 0; i < tokens.length; ++i ){
        token = tokens[i];

        if( token in map ){
            if( i === tokens.length - 1 )
                functionBody += `${map[ token ]( paramName, "", j )}`;
            else
                functionBody += `${map[ token ]( paramName, "", j )} + `;
            // console.log( functionBody );
            ++j;
        } else {
            path = _buildPath( paramName, `[${j}]` );
            strToken = `"${token}"`;
            if( i === tokens.length - 1 ){
                functionBody += strToken;
            } else{
                functionBody += `${strToken} + `;
            }
        }
    }

    return functionBody;
}

// see https://baymard.com/checkout-usability/credit-card-patterns for a more detailed list
function _buildCCFormatter( cardType, breakChar ){
    let ccType = ccTypes[ cardType ];

    // if( ccType === undefined )
    //     throw new Error( `No credit card company named ${cardType}` );

    let breaks = ccType.gaps;
    let lengths = ccType.lengths;
    let paramName = "arr";

    let map = {
        // d: digitToken_array
        d: digitToken_simple
    };

    let len = -1;
    let pattern = [];
    let brkIndex = {};
    let brkIndexes = [];
    let patterns = [];

    for( let k = 0; k < breaks.length; ++k ){
        brkIndex[ breaks[k] ] = true;
    }

    for( let i = 0; i < lengths.length; ++i ){
        brkIndexes.push( utils.copy( brkIndex ) );
    }

    // console.log( brkIndex );

    for( let j = 0; j < lengths.length; ++j ){

        len = lengths[j];
        brkIndex = brkIndexes.pop();

        for( let i = 0; i < len; ++i ){

            if( brkIndex[i] ){
                brkIndex[i] = false;

                pattern.push( breakChar );

                --i;
            } else {
                pattern.push( "d" );
            }

        }

        patterns.push( { len, pattern } );
        pattern = [];

    }

    // console.log( patterns );

    let swtch = `switch( ${paramName}.length ){`;

    while( patterns.length > 0 ){
        pattern = patterns.pop();
        len = pattern.len;
        pattern = pattern.pattern;

        // console.log( pattern );
        // console.log( len );

        swtch += _buildCase( len, _buildArrayFormatterBody( pattern, paramName, map, {} ) )
    }

    swtch += '}';

    return new Function( paramName, swtch );
}


function _buildCase( caseId, code ){
    return ` case ${caseId}: ${code}; `;
}

// let format = _buildCCFormatter( "americanExpress", "-" );
// console.log( format );
// console.log( format( [ 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7 ] ) );