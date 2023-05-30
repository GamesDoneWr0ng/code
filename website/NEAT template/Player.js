class Player {
    constructor() {
        this.fitness = 0;
        this.vision = []; // the input array fed into the neural network
        this.decision =  []; // the output of the neural network
        this.unadjustedFitness;
        this.lifespan = 0; // how long the player has lived for this.fitness
        this.bestScore = 0; // the best score ever achieved
        this.dead = false
        this.score = 0;
        this.gen = 0;

        this.genomeInputs = 5;
        this.genomeOutputs = 2;
        this.brain = new Genome(this.genomeInputs, this.genomeOutputs);
    }

    show() {
        // replace
    }

    move() {
        // replace
    }

    update() {
        // replace
    }

    look() {
        // replace
    }

    // gets the output of this.brain and converts them to actions
    think() {
        var max = 0;
        var maxIndex = 0;

        // get the output of the neural network
        this.decision = this.brain.feedForward(this.vision);

        for (var i = 0; i < this.decision.length; i++) { // find max and maxIndex
            if (this.decision[i] > max) {
                max = this.decision[i];
                maxIndex = i;
            }
        }

        // replace
    }

    // returns a clone of this player with the same brain
    clone() {
        var clone = new Player();
        clone.brain = this.brain.clone();
        clone.fitness = this.fitness;
        clone.brain.generateNetwork()
        clone.gen = this.gen;
        clone.bestScore = this.bestScore;

        return clone;
    }

    //since there is some randomness in games sometimes when we want to replay the game we need to remove that randomness
    //this fuction does that
    cloneForReplay() {
        var clone = this.clone();

        // replace
        
        return clone;
    }

    // calculates fitness score for evolution
    calculateFitness() {
        // replace
    }

    crossover(parrent2) {
        var child = new Player();
        if (this.fitness > parrent2.fitness) {
            child.brain = this.brain.crossover(parrent2.brain);
        } else {
            child.brain = parrent2.brain.crossover(this.brain);
        }

        child.brain.generateNetwork();
        return child;
    }
}