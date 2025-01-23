// var a = 3;
// var b = 1;

// var c = b;
// b = a;
// a = c;

// console.log("a", a, "b", b);

var a = 3;
var b = 1;

a = a ^ b;
b = a ^ b;
a = a ^ b;

console.log("a", a, "b", b);

var cube = n => n**2;
var trapes = (a,b,h) => (a+b)/2*h;

//console.log(cube(b))
console.log(trapes(1,2,3));