// console.log("oppg.2 alder")
// let alder = 20;

// if (alder >= 18) {
//     console.log("over 18");
// } else if (alder >= 16) {
//     console.log("over 16");
// } else {
//     console.log("ikke kjøre");
// }

// console.log("oppg.3 loop")
// for (let i = 2; i <= 30; i+=2) {
//     console.log(i)
// }

console.log("oppg.4 terning")
let terning = 0;
let antall = 0;

while (terning != 6) {
    terning = Math.floor(Math.random() * 6) +1;
    console.log(terning);
    antall++
}
console.log("antall", antall)