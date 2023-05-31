class Species {
    constructor(firstGenome) {
        this.players = [];
        this.bestFitness = 0;
        this.champ;
        this.averageFitness = 0;
        this.staleness = 0; //how many generations the species has gone without an improvement
        this.rep;

        this.excessCoeff = 1;
        this.weightDiffCoeff = 0.5;
        this.compatibilityThreshold = 3;

        if (firstGenome) {
            this.players.push(firstGenome);
            // since p is the only player in the species, it's the best fitness
            this.bestFitness = firstGenome.fitness;
            this.averageFitness = firstGenome.fitness;
            this.champ = firstGenome;
            this.rep = firstGenome.brain.clone()
        }
    }

    sameSpecies(genome) {
        var compatibility;
        var excessAndDisjoint = this.getExcessDisjoint(genome, this.rep); // get the number of excess and disjoint genes between this player and the current species this.rep
        var averageWeightDiff = this.getAverageWeightDiff(genome, this.rep); // get the average weight difference between matching genes

        var largeGenomeNormalizer = Math.max(genome.genes.length - 20, 1); 

        // compatibility formula
        compatibility = (this.excessCoeff * excessAndDisjoint / largeGenomeNormalizer) + (this.weightDiffCoeff * averageWeightDiff);
        return (this.compatibilityThreshold > compatibility);
    }

    // add a player to the species
    addToSpecies(genome) {
        this.players.push(genome);
    }

    //returns the number of excess and disjoint genes between the 2 input genomes
    //i.e. returns the number of genes which dont match
    getExcessDisjoint(brain1, brain2) {
        var matching = 0;
        for (var i = 0; i < brain1.genes.length; i++) {
            for (var j = 0; j < brain2.genes.length; j++) {
                if (brain1.genes[i].innovationNumber == brain2.genes[j].innovationNumber) {
                    matching++;
                    break;
                }
            }
        }
        return (brain1.genes.length + brain2.genes.length) - 2 * matching; // return number of excess and disjoin genes
    }
    
    // returns average weight difference between matching genes in the input genome
    getAverageWeightDiff(brain1, brain2) {
        if (brain1.genes.length == 0 || brain2.genes.length == 0) {
            return 0;
        }

        var matching = 0;
        var totalDiff = 0;
        for (var i = 0; i < brain1.genes.length; i++) {
            for (var j = 0; j < brain2.genes.length; j++) {
                if (brain1.genes[i].innovationNumber == brain2.genes[j].innovationNumber) {
                    matching++;
                    totalDiff += Math.abs(brain1.genes[i].weight - brain2.genes[j].weight);
                    break;
                }
            }
        }

        if (matching == 0) { // devide by 0 error
            return 100;
        }

        return totalDiff / matching; // average
    }

    // sorts the species by fitness
    sortSpecies() {
        this.players.sort((a, b) => {
            return b.fitness - a.fitness;
        });
    }
    
    setAverage() {
        for (var i = 0; i < this.players.length; i++) {
            this.players[i].calculateFitness();
        }
        var totalSum = this.players.reduce((sum, player) => sum + player.fitness, 0);

        this.averageFitness = totalSum / this.players.length;
    }

    //gets baby from the this.players in this species
    giveMeBaby(innovationHistory) {
        var baby;
        if (random(1) < 0.25) { // 25% of the time there is no crossover and the baby is a clone of a random ish player
            baby = this.selectPlayer().clone();
        } else { // 75% chance to do the crossover 
            // get two random ish parrents
            var parrent1 = this.selectPlayer();
            var parrent2 = this.selectPlayer();

            //the crossover function expects the highest fitness parent to be the object and the lowest as the argument
            if (parrent1.fitness > parrent2.fitness) {
                baby = parrent1.crossover(parrent2);
            } else {
                baby = parrent2.crossover(parrent1);
            }
            baby.brain.mutate(innovationHistory); // mutate that baby brain
        }
        return baby;
    }

    // selects a random player based on its fitness
    selectPlayer() {
        var fitnessSum = this.players.reduce((sum, player) => sum + player.fitness, 0); // sum of fittnesses

        var rand = random(fitnessSum);

        var runningSum = 0;
        for (var i = 0; i < this.players.length; i++) { // loop throgh each player
            runningSum += this.players[i].fitness;

            if (runningSum > rand) { // until it reaches the random number
                return this.players[i];
            }
        }

        return this.players[0] // ureachable statement to make parser happy
    }

    // kills of bottom half of the species
    cull() {
        if (this.players.length > 2) {
            this.sortSpecies();
            this.players.splice(floor(this.players.length  * 0.5), floor(this.players.length  * 0.5));
        }
    }

    //in order to protect unique this.players, the fitnesses of each player is divided by the number of this.players in the species that that player belongs to
    fitnessSharing() {
        for (var i = 0; i < this.players.length; i++) {
            this.players[i].fitness /= this.players.length;
        }
    }
}