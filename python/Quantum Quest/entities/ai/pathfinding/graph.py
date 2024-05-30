from entities.ai.pathfinding.node import Node
from math import inf

class Graph:
    def __init__(self, room) -> None:
        self.room = room
        self.nodes: list[Node] = []
        self.fillNodes()

    def fillNodes(self):
        pass

    def findPath(self, start, end):
        # find closest nodes
        minStart, minEnd = inf
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

        