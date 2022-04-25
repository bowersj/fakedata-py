const ccNum = require( "./creditCardNumbers" );
const ccv = require( "./ccv.js" );

module.exports = {
    visa: ccNum.visa,
    visaElectron: ccNum.visaElectron,
    mastercard: ccNum.masterCard,
    discover: ccNum.discoverCard,
    americanExpress: ccNum.americanExpress,
    unionpay: ccNum.unionPay,
    maestro: ccNum.maestro,
    elo: ccNum.elo,
    mir: ccNum.mir,
    hiper: ccNum.hiper,
    hipercard: ccNum.hipercard,
    ccv
};
