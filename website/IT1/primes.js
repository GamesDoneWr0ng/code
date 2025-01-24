let isPrime=n=>n%2===0?false:Array(Math.floor(Math.sqrt(n)/2)).keys().reduce((v,e)=>n<=(e*2+3)?true:v&&(n%(e*2+3))!==0,true);
let primes=n=>n<=3?[...Array(Math.max(0,n)).keys()].map(n=>n+1):[1].concat([false,false].concat(Array(n-2).fill(true)).reduce((v,p,i,a)=>p&&i<Math.sqrt(n)?(v===null?a:v).map((c,j)=>j>=i*i&&j%i==0?false:c):v,null).map((p,i)=>p?i:null).filter(n=>n!==null))

function primesLessThan(n) {
    if (n <= 3) return [...Array(Math.max(0,n)).keys()].map(n=>n+1);
    let sieve = Array(n).fill(true);
    sieve[0] = sieve[1] = false;
    let max = Math.sqrt(n);
    for (let i = 2; i < max; i++) {
        if (sieve[i]) {
            for (let j = i*i; j < n; j+=i) {
                sieve[j] = false;
            }
        }
    }
    return sieve
        .map((isPrime, index) => isPrime ? index : null)
        .filter(num => num !== null);
}
console.log([...Array(100).keys()].filter(isPrime));
console.log(primesLessThan(100));
console.log(primes(100));