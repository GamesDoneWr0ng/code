var population;
var nextConnectionNo = 1000;
var speed = 60; // fps

var showBest = true; //true if only show the best of the previous generation
var runBest = false; //true if replaying the best ever game

var showBrain = false;
var showBestEachGen = false;
var upToGen = 0;

var showNothing = false;

function setup() {
    window.canvas = createCanvas(1280, 720);

    population = new Population(500);
}

function draw() {
    drawToScreen();
    
    if (showBestEachGen) { // show the best of each gen
        showBestPlayersForEachGeneration();
    } else if (runBest) { // if replaying the best ever game
        showBestEverPlayer();
    } else { // just evolving noramly
        if (!population.done()) { //if any players are alive then update them
            population.updateAlive();
        } else { //all dead
            population.naturalSelection(); //genetic algorithm
        }
    }
}

function showBestPlayersForEachGeneration() {
    if (!genPlayerTemp.dead) { // If current gen player is not dead then update it
        genPlayerTemp.look();
        genPlayerTemp.think();
        genPlayerTemp.update();
        genPlayerTemp.show();
    } else { // if dead move onto the next generation
        upToGen++;
        if (upToGen >= population.genPlayers.lenght) { // If at the end then return to the start and stop doing it
            upToGen = 0;
            showBestEachGen = false;
        } else { // If not at the end then get the next generation
            genPlayerTemp = population.genPlayers[upToGen].cloneForReplay();
        }
    }
}

function showBestEverPlayer() {
    if (!population.bestPlayer.dead) { // If current gen player is not dead
        population.bestPlayer.look();
        population.bestPlayer.think();
        population.bestPlayer.update();
        population.bestPlayer.show();
    } else { // once dead
        runBest = false;
        population.bestPlayer = population.bestPlayer.cloneForReplay(); //reset the best player so it can play again
    }
}

function drawToScreen() {
    if (showNothing) {
        // replace

        drawBrain();
        writeInfo();
    }
}

function drawBrain() { // show the brain of whatever genome is currently showing
    var startX = 0; // replace
    var startY = 0;
    var w = 0;
    var h = 0;

    if (runBest) {
        population.bestPlayer.brain.drawGenome(startX, startY, w, h);
    } else if (showBestEachGen) {
        genPlayerTemp.brain.drawGenome(startX, startY, w, h);
    } else {
        population.players[0].brain.drawGenome(startX, startY, w, h);
    }
}

function writeInfo() { // replace
    fill(200);
    textAlign(LEFT);
    textSize(30);

    if (showBestEachGen) {
        text("Score: " + genPlayerTemp.score, 650, 50);
        text("Gen: " + genPlayerTemp.gen + 1, 1150, 50);
    } else if (runBest) {
        text("Score: " + population.bestPlayer.score, 650, 50);
        text("Gen: " + population.gen + 1, 1150, 50);
    } else if (showBest) {
        text("Score: " + population.players[0].score, 650, 50);
        text("Gen: " + population.gen + 1, 1150, 50);
    } 
}

function keyPressed() {
    switch(key) {
        case ' ': // toggle showbest
            showBest = !showBest;
            break
        case 'B':
            runBest = !runBest;
            break;
        case 'G':
            showBestEachGen = !showBestEachGen;
            upToGen = 0;
            genPlayerTemp = population.genPlayers[upToGen].clone();
            break;
        case 'N': // show nothing
            showNothing = !showNothing;
            break;
    }

    if (showBestEachGen) {
        switch (keyCode) {
            case LEFT_ARROW:
                upToGen--;
                if (upToGen < 0) {
                    showBestEachGen = false;
                } else {
                    genPlayerTemp = population.genPlayers[upToGen].cloneForReplay();
                }
                break;
            case RIGHT_ARROW:
                upToGen++;
                if (upToGen >= population.genPlayers.lenght) {
                    showBestEachGen = false;
                } else {
                    genPlayerTemp = population.genPlayers[upToGen].cloneForReplay();
                }
                break;
        }
    }
}