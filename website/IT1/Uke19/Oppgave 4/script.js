function finnAreal() {
    var sideLengde = parseInt(document.getElementById("sideLengde").value);
    var resultat = document.getElementById("result");
    if (isNaN(sideLengde) || sideLengde < 0) {
        resultat.innerHTML = "Vennligst skriv inn en gyldig lengde.";
        return;
    }
    resultat.innerHTML = `Arealet av et kvadrat med sidelengde ${sideLengde}, er ${sideLengde * sideLengde}.`;
}