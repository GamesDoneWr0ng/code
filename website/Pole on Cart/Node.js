class Node {
    constructor(number) {
        this.number = number;
        this.inputSum = 0;
        this.outputValue = 0;
        this.outputConnections = [];
        this.layer = 0;
        this.drawPos = createVector();
    }

    engage() {
        if (this.layer != 0) { // no activation function for inputs and bias
            this.outputValue = this.activation(this.inputSum);
        }

        for (var i = 0; i < this.outputConnections.length; i++) { // for each connection
            if (this.outputConnections[i].enabled) { //dont do shit if not enabled
                this.outputConnections[i].toNode.inputSum += this.outputConnections[i].weight * this.outputValue; //add the weighted output to the sum of the inputs of whatever node this node is connected to
            }
        }
    }

    activation(x) {
        // sigmoid
        return 1.0 / (1.0 + pow(Math.E, -4.9 * x))
    }

    //returns whether this node connected to the parameter node
    //used when adding a new connection
    isConnectedTo(node) {
        if(node.layer == this.layer) { //nodes in the same this.layer cannot be connected
            return false;
        }
  
        if (node.layer < this.layer) {
            for (var i = 0; i < node.outputConnections.length; i++) { // loop through parameter node's output nodes
                if (node.outputConnections[i].toNode == this) { // if this node is in the outputnodes
                    return true;
                }
            }
        } else {
            for (var i = 0; i < node.outputConnections.length; i++) { // loop through this node's output nodes
                if (node.outputConnections[i].toNode == this) { // if parameter node is in the outputnodes
                    return true;
                }
            }
        }

        return false; // The nodes aren't connected
      }

      // returns a copy of this node
      clone() {
        var clone = new Node(this.number);
        clone.layer = this.layer;
        return clone;
      }
}
