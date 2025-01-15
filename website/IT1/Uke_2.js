const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
await sleep(1000);


var input = "";
while (!(/^\d+$/.test(input)) || 1 > Number(input) || Number(input) > 50) {
    input = prompt("Skriv et tall 1-50:");
}
input = Number(input);

var antallSpill = "";
while (!(/^\d+$/.test(antallSpill)) || 1 > Number(antallSpill)) {
    antallSpill = prompt("Skriv antall forsøk:");
}
antallSpill = Number(antallSpill);

var i = 1;
do {
    var value = Math.floor(Math.random()*50+1);
    var treff = value === input;
    console.log(value, i);
    await sleep(200)
    i++;
} while (!treff && i <= antallSpill);

if (treff) {
    console.log(value, "Treff etter", i-1, "forsøk.");
} else {
    console.log("Traff aldri", input, "etter", antallSpill, "forsøk.");
}
}

main()