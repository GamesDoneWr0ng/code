//Array(10).keys().forEach(i=>{console.log(`Kvadratet av ${i} er ${i*i} og i fjerde ${i**4}`)});
let isPalindrome=text=>text.split("").reduce((v,e,i,a)=>v&&e===a[a.length-1-i],true);
let isPrime=n=>n%2===0?false:Array(Math.floor(Math.sqrt(n)/2)).keys().reduce((v,e)=>n<=(e*2+3)?true:v&&(n%(e*2+3))!==0,true);
let primesLessThan=n=>n<=3?[...Array(Math.max(0,n)).keys()].map(n=>n+1):[1].concat([false,false].concat(Array(n-2).fill(true)).reduce((v,p,i,a)=>p?(v===null?a:v).map((c,j)=>j>=i*i&&j%i==0?false:c):v,null).map((p,i)=>p?i:null).filter(n=>n!==null));
let swap=(a,b)=>[b,a];
let checkAlder=(n,a)=>console.log(`Hei ${n} du er ${a<30?"ung":"gammel"}`);

[...Array(10000).keys()].filter(isPrime).forEach(e=>console.log(e));
await Promise.all()