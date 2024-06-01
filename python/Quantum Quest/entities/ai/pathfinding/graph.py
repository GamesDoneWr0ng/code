from entities.ai.pathfinding.node import Node
import numpy as np

class Graph:
    def __init__(self, room, abilities) -> None:
        self.room = room
        self.abilities = abilities
        self.nodes: list[Node] = []
        self.fillNodes()

    def fillNodes(self):
        for object in self.room.objects:
            self.nodes.extend(object.getNodes())
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    node1.attemptConnect(node2, self.abilities)

    def findPath(self, start, end):
        # find closest nodes
        minStart = minEnd = np.inf
        startId, endId = None, None
        for node in self.nodes:
            if start**2 + node.pos**2 < minStart**2:
                minStart = start**2 + node.pos**2
                startId = node.id
            if end**2 + node.pos**2 < minEnd**2:
                minEnd = end**2 + node.pos**2
                endId = node.id
        
        startNode = self.nodes[startId]
        endNode = self.nodes[endId]

        openList: dict[int, Node] = {startId, startNode}
        closedList: dict[int, Node] = {}

        while len(openList) > 0:
            currentNode: Node = min(openList, key=lambda x: x.f)
            
            del openList[currentNode.id]
            closedList[currentNode.id] = currentNode

            # if we found the end
            if currentNode == endNode:
                path = []
                current = currentNode
                while current is not None:
                    path.append(current.pos)
                    current = current.parent
                return path[::-1]
            
            for child in currentNode.children:
                if closedList[child.id]:
                    continue
                
                child.g = currentNode.g + currentNode.children[node]
                child.h = np.linalg.norm(endNode.pos - child.pos) # TODO: estimate time
                child.f = child.g + child.h

                if openList[currentNode.id] and child.g >= openList[currentNode.id].g:
                    continue

                openList[child.id] = child