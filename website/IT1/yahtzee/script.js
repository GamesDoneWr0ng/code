const dice     = [...document.querySelectorAll(".die-list"   )].sort((a,b)=>a.id[4]-b.id[4]);
const switches = [...document.querySelectorAll(".roll-switch")].sort((a,b)=>a.id[7]-b.id[7]);
const diceValues = dice.map(e=>Number(e.getAttribute("data-roll")));

function rollDice() {
    dice.forEach((die, i) => {
        if (!switches[i].checked) {
          toggleClasses(die);
          let n = getRandomNumber(1, 6);
          die.dataset.roll = n;
          diceValues[i] = n;
        }
    });
}

function toggleClasses(die) {
    die.classList.toggle("odd-roll");
    die.classList.toggle("even-roll");
}

function getRandomNumber(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.getElementById("roll-button").addEventListener("click", rollDice);