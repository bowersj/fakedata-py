
module.exports = {
    threeDigit: threeDigit,
    fourDigit: fourDigit
};

function threeDigit(){
    return ( ( Math.floor( Math.random() * 9 ) + 1 ) * 100 ) + Math.floor( Math.random() * 100 );
}


function fourDigit(){
    return ( ( Math.floor( Math.random() * 9 ) + 1 ) * 1000 ) + Math.floor( Math.random() * 1000 );
}