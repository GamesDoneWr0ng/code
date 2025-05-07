var numberEl = document.getElementById("number_input");
var resultEl = document.getElementById("result");

function getSum() {
    var n = parseInt(numberEl.value);
    if (isNaN(n) || n < 2) {
        resultEl.innerHTML = "Vennligst skriv inn et gyldig tall større enn eller lik 2.";
        return;
    }
    var sum = 0;
    for (var i = 2; i <= n; i+=2) {
        sum += i;
    }
    resultEl.innerHTML = `Summen av alle partall fra 2 til ${n} er ${sum} <br>Gjennomsnittet er ${sum / Math.floor(n / 2)}`;
}