class Population {
    constructor (size) {
        this.players = [];
        this.bestPlayer;
        this.bestScore = 0;
        this.globalBestScore = 0;
        this.gen = 1;
        this.innovationHistory = [];
        this.genPlayers = [];
        this.species = [];

        this.massExtinctionEvent = false;
        this.newStage = false;

        for (var i = 0; i < size; i++) {
            this.players.push(new player());
            this.players[this.players.length - 1].brain.mutate(this.innovationHistory);
            this.players[this.players.length - 1].brain.generateNetwork();
        }
    }

    updateAlive() {
        for (var i = 0; i < this.players.length; i++) {
            if (!this.players[i].dead) {
                this.players[i].look() // get inputs for the brain
                this.players[i].think() // use the uotputs from the neuralnetwork
                this.players[i].update(); // update the player acording to the outputs from the neuralnetwork
                if (!showNothing && (!showBest || i == 0)) {
                    this.players[i].show(); // show the player
                }

                if (this.players[i].score > this.globalBestScore) { // update best score
                    this.globalBestScore = this.players[i].score;
                }
            }
        }
    }

    // returns true if all the players are dead :(
    done() {
        for (var i = 0; i < this.players.length; i++) {
            if (!this.players[i].dead) {
                return false;
            }
        }
        return true;
    }

    // sets the best player for this.gen
    setBestPlayer() {
        var tempBest = this.species[0].players[0];
        tempBest.gen = this.gen;

        // if the best of this.gen is beter then the global best score then update the global best score
        if (tempBest.score >= this.bestScore) {
            this.genPlayers.push(tempBest.cloneForReplay());
            console.log("old best: " + this.bestScore);
            console.log("new best: " + tempBest.score);
            this.bestScore = tempBest.score;
            this.bestPlayer = tempBest.cloneForReplay();
        }
    }

    // this funcion is called when all the players in this generation are dead and a new this.gen needs to be made
    natrualSelection() {
        var previousBest = this.players[0];
        this.speciate(); // separate this.players into species
        this.calculateFitness(); // calculate the fitness of each player
        this.sortSpecies(); // sort the species by fitness, best first

        if (this.massExtinctionEvent) {
            this.massExtinction();
            this.massExtinctionEvent = false;
        }

        this.cullSpecies(); // kill of the bottom half of each species
        this.setBestPlayer(); // save the best player of this.gen
        this.killStaleSpecies(); // kill of the species which haven't improved in the last 15(ish) generations
        this.killBadSpecies(); // kill of the species which are so bad they can't reproduce

        console.log("Generation: " + this.gen + " Number of Mutations: " + this.innovationHistory.length + " Species: " + this.species.length);

        var averageSum = this.getAvgFitnessSum();
        var children = [];
        for (var i = 0; i < this.species.length; i++) { // for each species
            children.push(this.species[i].champ.clone()) // add the champ without any mutations
            var NumberOfChilden = floor(this.species[i].averageFitness / averageSum * this.players.length) - 1; // the number of children that this species is allowed
            for (var j = 0; j < NumberOfChilden; j++) { // for each child
                children.push(this.species[i].giveMeBaby(this.innovationHistory)); // add the child
            }
        }

        if (children.length < this.players.length) { // if there are less children than players
            children.push(previousBest.clone())
        }

        while (children.length < this.players.length) { // if there are less children than players due to flooring
            children.push(this.species[0].giveMeBaby(this.innovationHistory)); // add a child from the best species
        }

        this.players = [];
        arrayCopy(children, this.players); // set the children as the current players
        this.gen++; // increment the generation
        for (var i = 0; i < this.players.length; i++) { // generate networks for each of the children
            this.players[i].brain.generateNetwork();
        }
    }

    // separate players into species based on how similar they are to the species leader of each this.species in the previous this.gen
    speciate() {
        for (var s of this.species) { // empty this.species
            s.players = [];
        }

        for (var i = 0; i < this.players.length; i++) { // for each player
            var speciesFound = false;
            for (var s of this.species) { // for each species
                s.addToSpecies(this.players[i]); // add the player to the species
                speciesFound = true;
                break;
            }
        }
        if (!speciesFound) { // if no species were found add a new species with this as its champion
            this.species.push(new Species(this.players[i]));
        }
    }
    
    // calculate the fitness of each player
    calculateFitness() {
        // sort the players within a this.species
        for (var s of this.species) {
            s.sortSpecies();
        }

        // sort the species by the fitness of the best player, best first
        this.species.sort((a, b) => {
            return b.bestFitness - a.bestFitness;
        });
    }

    // If a species sucks so much that it wont even be allocated 1 child for the next this.gen then kill it now
    killBadSpecies() {
        var averageSum = this.getAvgFitnessSum();

        for (var i = 1; i < this.species.length; i++) {
            if (this.species[i].averageFitness / averageSum * this.players.length < 1) { // if it wont be given a single child
                this.species.splice(i, 1);

                i--;
            }
        }
    }

    // returns the sum of each this.species average fitness
    getAvgFitnessSum() {
        return this.species.reduce((sum, s) => sum + s.averageFitness, 0);
    }

    // kill the bottom half of each species
    cullSpecies() {
        for (var s of this.species) {
            s.cull(); // kill bottom half
            s.fitnessSharing(); // also while we're at it lets do fitness sharing
            s.setAverage(); // reset avreges because they have changed
        }
    }

    // kill all but best 5 species
    massExtinction() {
        this.species.splice(5, this.species.length - 5);
    }
    
    // batch learning
    // update all alive players
    updateAliveInBatches() {
        var aliveCount = 0;
        for (var i = 0; i < this.players.length; i++) {
            if (this.playerInBatch(this.players[i])) {
                if (!this.players[i].dead) {
                    aliveCount++;
                    this.players[i].look() // get inputs for the brain
                    this.players[i].think() // use the uotputs from the neuralnetwork
                    this.players[i].update(); // update the player acording to the outputs from the neuralnetwork

                    if (!showNothing && (!showBest || i == 0)) {
                        this.players[i].show(); // show the player
                    }

                    if (this.players[i].score > this.globalBestScore) { // update best score
                        this.globalBestScore = this.players[i].score;
                    }
                }
            }
        }

        if (aliveCount == 0) {
            this.batchNo++;
    }
}

    // returns true if the player is in the batch
    playerInBatch(player) {
        for (var i = this.batchNo * this.worldsPerBatch; i < min((this.batchNo + 1) * this.worldsPerBatch, worlds.length); i++) {
            if (player.world == worlds[i]) {
                return true;
            }
        }

        return false;
    }

    stepWorldsInBatch() {
        for (var i = this.batchNo * this.worldsPerBatch; i < min((this.batchNo + 1) * this.worldsPerBatch, worlds.length); i++) {
            worlds[i].step(1 / 30, 10, 10);
        }
    }

    // returns true if all the players are dead :(
    batchDead() {
        for (var i = this.batchNo * this.playersPerBatch; i < min((this.batchNo + 1) * this.playersPerBatch, this.players.length); i++) {
            if (!this.players[i].dead) {
                return false;
            }
        }
        
        return true;
    }
}