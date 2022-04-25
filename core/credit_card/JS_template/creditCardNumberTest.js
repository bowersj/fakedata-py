const stats = require( "../../stats/base.js" );
const gen = require( "./creditCardNumbers.js" );
const perf = require( "./../performance.js" );

// let valid_credit_card = require( 'card-validator' );
// let cc = gen.hipercard();
// console.log( cc );
// console.log( cc.length );
// console.log( valid_credit_card.number( cc.join( "" ) ) );

console.log( perf.runTests(
    [ { func: gen.visa, name: "visa" },
        { func: gen.visaElectron, name: "visaElectron"},
        { func: gen.masterCard, name: "masterCard" },
        { func: gen.discoverCard, name: "discoverCard" },
        { func: gen.americanExpress, name: "americanExpress" },
        { func: gen.unionPay, name: "unionPay" },
        { func: gen.maestro, name: "maestro" },
        { func: gen.elo, name: "elo" },
        { func: gen.mir, name: "mir" },
        { func: gen.hiper, name: "hiper" },
        { func: gen.hipercard, name: "hipercard" }
    ],
    // [ gen.visa, gen.visaElectron, gen.masterCard ],
    { samples: 3000000 }
    )
);
