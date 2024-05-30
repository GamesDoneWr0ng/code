from typing import Self
from math import inf


class Node:
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        self.distance = -inf
        self.cost = inf

        self.parents = []
        self.children = []

    def __eq__(self, __value: Self) -> bool:
        return self.id == __value.id

    def addParent(self, parent):
        self.parents.append(parent)

    def attemptConnect(self, node: Self, abilities):
        if node in self.children:
            return
        
        for ability in abilities:
            posible, cost = ability.canConnect(self.pos, node.pos)
            if posible and node.cost > cost:
                node.cost = cost
                node.addParent(self)
                self.children.append(node)