// bank identification varies by country, see link below for details
// https://en.wikipedia.org/wiki/Bank_code

module.exports.accountNumber = genAccountNumber;
module.exports.routingNumber = genRoutingNumber;

function genRoutingNumber() {
    return Math.floor(Math.random()*100000000);
}


function genAccountNumber(){
    return Math.floor(Math.random()*100000000000);
}