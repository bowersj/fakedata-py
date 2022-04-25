
const utils = require( "../utils.js" );
const ccv = require( "./ccv.js" );

for( let i = 0; i < 1000000; ++i ){
    let num = ccv.threeDigit();
    let digits = utils.getDigits( num );
    if( digits.length !== 3 ){
        console.log( "more, or less, than three digits were generated" );
        console.log( num );
        console.log( digits );
        break;
    }
}


for( let i = 0; i < 1000000; ++i ){
    let num = ccv.fourDigit();
    let digits = utils.getDigits( num );
    if( utils.getDigits( num ).length !== 4 ){
        console.log( "more, or less, than four digits were generated" );
        console.log( num );
        console.log( digits );
        break;
    }
}

console.log( "The correct number of digits were generated every time." );