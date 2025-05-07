function checkAge() {
    var age = parseInt(document.getElementById("age").value);
    var result = document.getElementById("result");
    if (isNaN(age) || age < 0) {
        result.innerHTML = "Vennligst skriv inn en gyldig alder.";
        return;
    }
    if (age > 3 && age < 100) {
        result.innerHTML = "Du er gammel nok til å leke med lego";
    } else {
        result.innerHTML = "Du er ikke riktig alder for å leke med lego";
    }
}