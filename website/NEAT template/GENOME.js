class Genome {
    constructor(inputs, outputs, crossover) {
        this.genes = []; // A list of connections between this.nodes which represent the NN
        this.nodes = [];
        this.inputs = inputs;
        this.outputs = outputs;
        this.layers = 2;
        this.nextNode = 0;
        this.network = [];

        if (crossover) {
            return;
        }

        // create the input nodes
        for (var i = 0; i < inputs; i++) {
            this.nodes.push(new Node(i))
            this.nextNode++;
            this.nodes[i].layer = 0;
        }

        // create the output nodes
        for (var i = 0; i < outputs; i++) {
            this.nodes.push(new Node(i + inputs))
            this.nextNode++;
            this.nodes[i + inputs].layer = 1;
        }

        // Bias node
        this.nodes.push(new Node(this.nextNode));
        this.biasNode = this.nextNode;
        this.nextNode++;
        this.nodes[this.biasNode].layer = 0;
    }

    fullyConnect(innovationHistory) {
        //this will be a new number if no identical genome has mutated in the same
        for (var i = 0; i < this.inputs; i++) {
            for (var j = 0; j < this.outputs; j++) {
                var connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.nodes[i], this.nodes[this.nodes.length - j - 2])
                this.genes.push(new connectionGene(this.nodes[i], this.nodes[this.nodes.length - j - 2], random(-1, 1), connectionInnovationNumber))
            }
        }
    
        var connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.nodes[this.biasNode], this.nodes[this.nodes.length - 2]);
        this.genes.push(new connectionGene(this.nodes[this.biasNode], this.nodes[this.nodes.length - 2], random(-1, 1), connectionInnovationNumber));

        connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.nodes[this.biasNode], this.nodes[this.nodes.length - 3]);
        this.genes.push(new connectionGene(this.nodes[this.biasNode], this.nodes[this.nodes.length - 3], random(-1, 1), connectionInnovationNumber));

        this.connectNodes();
    }

    // returns the node with a matching number
    getNode(number) {
        for (var i = 0; i < this.nodes.length; i++) {
            if (this.nodes[i].number == number) {
                return this.nodes[i];
            }
        }
        return null;
    }

    connectNodes() {
        for (var i = 0; i < this.nodes.length; i++) {
            this.nodes[i].outputConnections = [];
        }
        
        for (var i = 0; i < this.genes.length; i++) {
            this.genes[i].fromNode.outputConnections.push(this.genes[i]);
        }
    }

    feedForward(inputValues) {
        for (var i = 0; i < this.inputs; i++) {
            this.nodes[i].outputValue = inputValues[i];
        }
        this.nodes[this.biasNode].outputValue = 1; // Output of bias is 1

        for (var i = 0; i < this.network.length; i++) {
            this.network[i].engage();
        }
    
        var outs = [];
        for (var i = 0; i < this.outputs; i++) {
            outs[i] = this.nodes[this.inputs + i].outputValue;
        }

        return outs;
    }

    generateNetwork() { // sets up the network
        this.connectNodes();
        this.network = [];
        for (var l = 0; i < this.layers; l++) { // for each layer
            for (var i = 0; i < this.nodes.length; i++) { // for each node
                if (this.nodes[i].layer == l) { // if node is in that layer
                    this.network.push(this.nodes[i]);
                }
            }
        }
    }

    //mutate the NN by adding a new node
    //it does this by picking a random connection and disabling it then 2 new connections are added
    //1 between the input node of the disabled connection and the new node
    //and the other between the new node and the output of the disabled connection
    addNode(innovationHistory) {
        if (this.genes.length == 0) {
            return;
        }

        do { // dont disconect bias
            var randomConnection = floor(random(this.genes.length));
        } while (this.genes[randomConnection].fromNode == this.nodes[this.biasNode] && this.genes.length != 1)

        this.genes[randomConnection].enabled = false; // disable the connection

        var newNodeNumber = this.nextNode;

        this.nodes.push(new Node(newNodeNumber));
        this.nextNode++;
        // add a new connection to the new node with a weight of 1
        var connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.genes[randomConnection].fromNode, this.getNode(newNodeNumber));
        this.genes.push(new connectionGene(this.genes[randomConnection].fromNode, this.getNode(newNodeNumber), 1, connectionInnovationNumber));

        connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.getNode(newNodeNumber), this.genes[randomConnection].toNode);
        // add a new connection from the new node with the same weight as the old connection
        this.genes.push(new connectionGene(this.getNode(newNodeNumber), this.genes[randomConnection].toNode, this.genes[randomConnection].weight, connectionInnovationNumber));
        this.getNode(newNodeNumber).layer = this.genes[randomConnection].fromNode.layer + 1;

        connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.nodes[this.biasNode], this.getNode(newNodeNumber));
        // connect the bias to the new node with a weight of 0
        this.genes.push(new connectionGene(this.nodes[this.biasNode], this.getNode(newNodeNumber), 0, connectionInnovationNumber));
    
        //if the layer of the new node is equal to the layer of the output node of the old connection then a new layer needs to be created
        //more accurately the layer numbers of all layers equal to or greater than this new node need to be incrimented
        if (this.getNode(newNodeNumber).layer == this.genes[randomConnection].toNode.layer) {
            for (var i = 0; i < this.nodes.length - 1; i++) {
                if (this.nodes[i].layer >= this.getNode(newNodeNumber).layer) {
                    this.nodes[i].layer++;
                }
            }
            this.layers++;
        }
        this.connectNodes();
    }

    // adds a connection between 2 nodes that aren't currently connected
    addConnection(innovationHistory) {
        // network is already fully connected
        if (this.fullyConnected()) {
            console.log("connection failed")
            return;
        }

        // get random nodes
        do {
            randomNode1 = floor(random(this.nodes.length));
            randomNode2 = floor(random(this.nodes.length));
        } while (checkValidConnection(randomNode1, randomNode2))

        if (this.nodes[randomNode1].layer > this.nodes[randomNode2].layer) {
            var temp = randomNode1;
            randomNode1 = randomNode2;
            randomNode2 = temp;
        }

        //get the innovation number of the connection
        //this will be a new number if no identical genome has mutated in the same way
        var connectionInnovationNumber = this.getInnovationNumber(innovationHistory, this.nodes[randomNode1], this.nodes[randomNode2]);

        // create the connection
        this.genes.push(new connectionGene(this.nodes[randomNode1], this.nodes[randomNode2], random(-1, 1), connectionInnovationNumber));
        this.connectNodes();

        // add the connection
        this.genes.push(new connectionGene(this.nodes[randomNode1], this.nodes[randomNode2], random(-1, 1), connectionInnovationNumber));
        this.connectNodes();
    }
    
    checkValidConnection(r1, r2) {
        if (this.nodes[r1].layer == this.nodes[r2].layer) return true; // nodes are in the same layer
        if (this.nodes[r1].isConnectedTo(this.nodes[r2])) return true; // nodes are already connected
 
        return false;
    }

    getInnovationNumber(innovationHistory, from, to) {
        var isNew = true;
        var connectionInnovationNumber = nextConnectionNo;
        for (var i = 0; i < innovationHistory.length; i++) {
            if (innovationHistory[i].matches(this, from, to)) {
                isNew = false;
                connectionInnovationNumber = innovationHistory[i].innovationNumber;
                break;
            }
        }

        if (isNew) { // if the mutation is new
            var innoNumbers = [];
            for (var i = 0; i < this.genes.length; i++) { // set the innovation number
                innoNumbers.push(this.genes[i].innovationNumber);
            }

            innovationHistory.push(new connectionHistory(from, to, connectionInnovationNumber, innoNumbers));
            nextConnectionNo++;
        }
        return connectionInnovationNumber;
    }
    
    // returns wheter the network is fully connected or not
    fullyConnected() {
        var  maxConnections = 0;
        var nodesInLayers = []; // array of amount of nodes in each layer
        for (var i = 0; i < this.layers; i++) {
            nodesInLayers[i] = 0;
        }
        // populate array
        for (var i = 0; i < this.nodes.length; i++) {
            nodesInLayers[this.nodes[i].layer]++;
        }

        //for each layer the maximum amount of connections is the number in this layer * the number of this.nodes infront of it
        //so lets add the max for each layer together and then we will get the maximum amount of connections in the network
        for (var i = 0; i < this.layers - 1; i++) {
            var nodesInFront = 0;
            for (var j = i +1; j < this.layers; j++) { // for each layer in front of this layer
                nodesInFront += nodesInLayers[j]; // add the amount of nodes in the layer
            }

            maxConnections += nodesInLayers[i] * nodesInFront;
        }

        if (maxConnections <= this.genes.length) {
            return true;
        } else {
            return false;
        }
    }

    // mutates the genome
    mutate(innovationHistory) {
        if (this.genes.length == 0) {
            this.addConnection(innovationHistory);
        }

        // 80% of the time mutate weights
        var rand1 = random(1);
        if (rand1 < 0.8) {
            this.mutateWeight();
        }

        // 5% of the time add a new connection
        var rand2 = random(1);
        if (rand2 < 0.05) {
            this.addConnection(innovationHistory);
        }

        // 1% of the time add a new node
        var rand3 = random(1);
        if (rand3 < 0.01) {
            this.addNode(innovationHistory);
        }
    }

    //called when this Genome is better that the other parent
    crossover(parrent2) {
        var child = new Genome(this.inputs, this.outputs, true);
        child.genes = [];
        child.nodes = [];
        child.layers = this.layers;
        child.nextNode = this.nextNode;
        child.biasNode = this.biasNode;
        var childGenes = [];
        var isEnabled = [];

        // innherit genes
        for (var i = 0; i < this.genes.length; i++) {
            var setEnabled = true; // is this node in the child going to be enabled

            var parent2gene = this.matchingGene(parrent2, this.genes[i].innovationNumber);
            if (parent2gene != -1) { // if the gene matches
                if (!this.genes[i].enabled || !parrent2.genes[parent2gene].enabled) { // if either parent is disabled
                    if (random(1) < 0.75) { // 75% chance of being disabled
                        setEnabled = false;
                    }
                }

                var rand = random(1);
                if (rand < 0.5) { // 50% chance of inheriting gene from parrent1
                    childGenes.push(this.genes[i]);
                } else {
                    childGenes.push(parrent2.genes[parent2gene]);
                }
            } else { // if the gene doesn't match
                childGenes.push(this.genes[i]);
                setEnabled = this.genes[i].enabled;
            }
            isEnabled.push(setEnabled);
        }
        
        //since all excess and difrent genes are inherrited from the more fit parent (this Genome) the childs structure is no different from this parent | with exception of dormant connections being enabled but this wont effect this.nodes
        //so all the this.nodes can be inherrited from this parent
        for (var i = 0; i < this.nodes.length; i++) {
            child.nodes.push(this.nodes[i].clone());
        }

        //clone all the connections so that they connect the childs new this.nodes
        for (var i = 0; i < childGenes.length; i++) {
            child.genes.push(childGenes[i].clone(child.getNode(childGenes[i].fromNode.number), child.getNode(childGenes[i].toNode.number)));
            child.genes[i].enabled = isEnabled[i];
        }

        child.connectNodes();
        return child;
    }

    // returns wheter or not there is a gene matching the innovationNumber in the input genome
    matchingGene(parrent2, innovationNumber) {
        for (var i = 0; i < parrent2.genes.length; i++) {
            if (parrent2.genes[i].innovationNumber == innovationNumber) {
                return i;
            }
        }
        return -1;
    }

    // print out info about the genome to the console
    printGenome() {
        console.log("Prvar genome layers: " + this.layers);
        console.log("Bias node: " + this.biasNode);
        console.log("this.nodes:");
        for (var i = 0; i < this.nodes.length; i++) {
            console.log(this.nodes[i].number + ",");
        }
        console.log("this.genes:");
        for (var i = 0; i < this.genes.length; i++) {
            console.log("Gene: " + this.genes[i].innovationNumber + " From node: ", fromNode + " To node: " + toNode + " Is enabled: " + this.genes[i].enabled +
            " From layer: " + this.genes[i].fromNode.layer + " To layer: " + this.genes[i].toNode.layer + " Weight: " + this.genes[i].weight);
        }

        console.log()
    }

    // returns a copy of this genome
    clone() {
        var clone = new Genome(this.inputs, this.outputs, true);

        // copy nodes
        for (var i = 0; i < this.nodes.length; i++) {
            clone.nodes.push(this.nodes[i].clone());
        }

        // copy genes
        for (var i = 0; i < this.genes.length; i++) {
            clone.genes.push(this.genes[i].clone(clone.getNode(this.genes[i].fromNode.number), clone.getNode(this.genes[i].toNode.number)));
        }

        clone.layers = this.layers;
        clone.nextNode = this.nextNode;
        clone.biasNode = this.biasNode;
        clone.connectNodes();

        return clone;
    }

    // draw the genome on the screen
    drawGenome(startX, startY, w, h) {
        var allNodes = [];
        var nodePositions = [];
        var nodeNumbers = [];

        for (var i = 0; i < this.layers; i++) {
            var temp = [];
            for (var j = 0; j < this.nodes.length; j++) { // for each node
                if (this.nodes[j].layer == i) { // check if it is in this layer
                    temp.push(this.nodes[j]); // add it to this layer
                }
            }
        }

        //for each layer add the position of the node on the screen to the positions array
        for (var i = 0; i < this.layers; i++) {
            fill(255, 0, 0);
            var x = startX + float((i + 1.0) * w) / float(this.layers + 1.0);
            for (var j = 0; j < allNodes[i].length; j++) {
                var y = startY + float((j + 1.0) * h) / float(allNodes[i].length + 1.0);
                nodePositions.push(createVector(x, y));
                nodeNumbers.push(allNodes[i][j].number)
            }
        }

        // draw connections
        stroke(0);
        strokeWeight(2);
        for (var i = 0; i < this.genes.length; i++) {
            if (this.genes[i].enabled) {
                stroke(0);
            } else {
                stroke(100);
            }
            
            var from;
            var to;
            from = nodePositions[nodeNumbers.indexOf(this.genes[i].fromNode.number)];
            to = nodePositions[nodeNumbers.indexOf(this.genes[i].toNode.number)];

            if (this.genes[i].weight > 0) {
                stroke(255, 0, 0);
            } else {
                stroke(0, 0, 255);
            }

            strokeWeight(map(abs(this.genes[i].weight), 0, 1, 0, 3));
            line(from.x, from.y, to.x, to.y);
        }

        //draw this.nodes last so they appear ontop of the connection lines
        for (var i = 0; i < nodePositions.length; i++) {
            fill(255);
            stroke(0);
            strokeWeight(1);
            ellipse(nodePositions[i].x, nodePositions[i].y, 20, 20);
            textSize(10);
            fill(0);
            textAlign(CENTER, CENTER);
            text(nodeNumbers[i], nodePositions[i].x, nodePositions[i].y);
        }
    }
}