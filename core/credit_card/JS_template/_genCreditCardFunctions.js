/**
 * This module generates the UnionPay credit card module.
 *
 * I went with code generation because there are 6 lengths with 20 patterns
 * to account for. This means there are 120 functions that need to be created.
 * That is a lot especially since most of the functions are permutations.
 *
 */
const fs = require( "fs" );
const path = require( "path" );
const utils = require( "../utils.js" );
const types = require( "./ccTypes.js" );
let valid_credit_card = require( 'card-validator' );


// let _funcs = [];
//
// for(let i = 0; i < types.length; ++i){
//     [].push.apply( _funcs, utils.buildCreditCardFunctions( types[i] ) );
// }
//
// console.log( "Functions to Test:", _funcs.length );
// let cc;
// let res;
// let shouldStop = false;
//
// for( let i = 0; i < _funcs.length; ++i ){
//     cc = _funcs[i]();
//
//     for( let j = 0; j < 100; ++j ){
//         res = valid_credit_card.number( cc.number.join( "" ) );
//         shouldStop = res.card === null || !res.isValid || res.card.type !== cc.type;
//         if( shouldStop )
//             break;
//     }
//
//     if( shouldStop )
//         break;
// }
//
// if( shouldStop ){
//     console.log( "No card", res.card === null );
//     console.log( "Not valid card", !res.isValid );
//     console.log( "Not Same Credit Card Type", res.card === null || res.card.type !== cc.type );
//     console.log( "Something went wrong..." );
//     console.log( "generated number", cc );
//     console.log( "Result of validation", res );
// } else {
//     console.log( "Everything worked!" );
// }

let cc = [6,2,5,2,5,7,8,9,6,7,1,1,0,6,0,7];
console.log( cc );
console.log( cc.length );
console.log( valid_credit_card.number( cc.join( "" ) ) );

// module.exports.generated = _genAmericanExpress37;

// let length = 0;
//
// for( let i = 0; i < len; ++i ){
//     length = lengths[i];
//
//
//     for( let j = 0; j < patterns.length; ++j ){
//
//     }
//
// }
