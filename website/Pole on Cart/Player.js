class Player {
    constructor() {
        this.fitness = 0;
        this.vision = []; // the input array fed into the neural network
        this.decition =  []; // the output of the neural network
        this.unadjustedFitness;
        this.lifespan = 0; // how long the player has lived for this.fitness
        this.bestScore = 0; // the best score ever achieved
        this.dead = false
        this.score = 0;
        this.gen = 0;

        this.genomeInputs = 4;
        this.genomeOutputs = 1;
        this.brain = new Genome(this.genomeInputs, this.genomeOutputs);

        // game
        this.cartPos = 640;
        this.poleAngle = 0;
        this.velocity = 0;
        this.poleVelocity = 0;
    }

    show() {
        background(220);
        fill(255);
        rectMode(CENTER);
        rect(this.cartPos, height - 300, 100, 40);

        // draw the pole
        let poleLength = 200;
        let poleWidth = 20;
        let pivotX = this.cartPos;
        let pivotY = height - 300;
        let poleEndX = pivotX + poleLength * sin(this.poleAngle);
        let poleEndY = pivotY - poleLength * cos(this.poleAngle);

        stroke(0);
        strokeWeight(poleWidth);
        line(pivotX, pivotY, poleEndX, poleEndY);

        this.brain.drawGenome(10, 10, 200, 200)
    }

    move() {
        if (!this.dead) {
            this.cartPos += this.velocity * 5;
        }
    }

    update() {
        this.lifespan++;
        this.score++;
        this.move();

        // check death
        if (this.cartPos < 0 || this.cartPos > width || this.poleAngle < -1 || this.poleAngle > 1) {
            this.dead = true;
            this.velocity = 0;
            this.poleAngle = 0;
            this.poleVelocity = 0;
            this.cartPos = 640;
        }

        // rotate pole
        const poleAcceleration = (0.1 * sin(this.poleAngle)) / 100 - (this.velocity * cos(this.poleAngle)) / 100;

        this.poleVelocity += poleAcceleration;
        if (this.poleVelocity < 0.001 && this.poleVelocity > -0.001) {
            this.poleVelocity += random(-0.01, 0.01);
        }
        this.poleAngle += this.poleVelocity;
    }

    look() {
        this.vision = [];
        this.vision.push(this.cartPos / 1280);
        this.vision.push(this.poleAngle / 0.5);
        this.vision.push(this.velocity / 10);
        this.vision.push(this.poleVelocity / 10);
    }

    // gets the output of this.brain and converts them to actions
    think() {
        this.decition = this.brain.feedForward(this.vision); // get the output

        this.velocity += this.decition[0] * 2 - 1; // decition is 0 to 1 so we make it -1 to 1 for the direction
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
        this.fitness = this.score;
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