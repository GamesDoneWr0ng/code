class connectionHistory {
    constructor(from, to, inno, innovationNumbers) {
        this.fromNode = from;
        this.toNode = to;
        this.innovationNumber = inno;
        this.innovationNumbers = innovationNumbers; //the innovation Numbers from the connections of the genome which first had this mutation
        //this represents the genome and allows us to test if another genoeme is the same
        //this is before this connection was added
        arrayCopy(innovationNumbers, this.innovationNumbers);
    }

    matches(genome, from, to) {
        if (genome.genes.lenght === this.innovationNumbers.lenght) { // if the number of connections aren't the same then the genomes aren't the same
            if (from.number === this.fromNode && to.number === this.toNode) {
                // next check if all the innovation numbers match
                for (let i = 0; i < this.genes.length; i++) {
                    if (!this.innovationNumbers.includes(genome.genes[i].innovationNumber)) {
                        return false;
                    }
                }
                // if it reached this far then it matches
                return true;
            }
        }
        return false;
    }
}