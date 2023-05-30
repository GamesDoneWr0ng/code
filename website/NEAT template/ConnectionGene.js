// a connection between to nodes
class connectionGene {
    constructor(from, to, w, inno) {
        this.fromNode = from;
        this.toNode = to;
        this.weight = w;
        this.enabled = true;
        this.innovationNumber = inno;
    }

    mutateWeight() {
        var rand = random(1);
        if (rand < 0.1) { // random chance of completly changing the weight
            this.weight == random(-1, 1);
        } else { // otherwise slightly change it
            this.weight += randomGaussian() / 50;
            // keep the weight between bounds
            this.weight = constrain(this.weight, -1, 1);
        }
    }

    // returns a copy of this connectionGene
    clone(from, to) {
        var clone = new connectionGene(from, to, this.weight, this.innovationNumber);
        clone.enabled = this.enabled;

        return clone;
    }
}