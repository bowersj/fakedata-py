// found at https://gist.github.com/shawndumas/1262659
module.exports = getSoundex;

function getSoundex( s ){
    let a = s.toLowerCase().split(''),
        f = a.shift(),
        r = '',
        codes = {
            a: '', e: '', i: '', o: '', u: '',
            b: 1, f: 1, p: 1, v: 1,
            c: 2, g: 2, j: 2, k: 2, q: 2, s: 2, x: 2, z: 2,
            d: 3, t: 3,
            l: 4,
            m: 5, n: 5,
            r: 6
        };

    r = f +
        a
            .map( value => codes[value] )
            .filter(function ( value, index, arr ) {
                return ((index === 0) ? value !== codes[f] : value !== arr[index - 1]);
            })
            .join('');

    return (r + '000').slice(0, 4).toUpperCase();
}