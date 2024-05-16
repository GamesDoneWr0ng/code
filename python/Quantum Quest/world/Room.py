from entities.Entity import Entity
from entities import EntityType
from entities.RemovalReason import RemovalReason
from entities.PlayerEntity import PlayerEntity
from world.objects.Object import Object
import numpy as np

class Room:
    def __init__(self, id: str, neighbours: list[str], dataFile: str) -> None:
        self.id: str = id
        self.neighbours: list[str] = neighbours
        self.dataFile: str = dataFile
        self.world = None

        self.player: PlayerEntity = None

        self.currentEntityId: int = -1
        self.entities: list[Entity] = [] # TODO: load from file
        self.objects:  list[Object] = []

        self.load()

    def getPlayer(self) -> PlayerEntity:
        return self.player

    def setWorld(self, world) -> None:
        self.world = world

    def getId(self) -> str:
        return self.id
    
    def nextId(self) -> int:
        return self.world.nextId()
    
    def getNeighbours(self) -> list[str]:
        return self.neighbours
    
    def getNeighboursWithout(self, neighbour: str) -> list[str]:
        return [n for n in self.neighbours if n != neighbour]
    
    def addEntity(self, entity: Entity) -> None:
        self.entities.append(entity)
        if entity.getType() == EntityType.PLAYER:
            self.player = entity

    def removeEntity(self, entity: Entity, reason: RemovalReason) -> None:
        entity.remove(reason) # TODO: removalreason
        self.entities.remove(entity)

    def addObject(self, object: Object) -> None:
        self.objects.append(object)
    
    def tick(self) -> None:
        for entity in self.entities:
            entity.tick()

        for object in self.objects:
            if object.isTicking() or object.isTrigger():
                object.tick()

    def emitGameEvent(self, event, pos: np.ndarray) -> None:
        self.world.emitGameEvent(event, pos)

    def recieveGameEvent(self, event, pos: np.ndarray) -> None:
        for entity in self.entities:
            entity.recieveGameEvent(event, pos)

    def render(self, screen, camera, scale: float) -> None:
        for object in self.objects:
            object.render(screen, camera, scale)

        for entity in self.entities:
            entity.render(screen, camera, scale)

    def getDeltaTime(self) -> float:
        return self.world.getDeltaTime()

    # load and save room data to file.
    def load(self):
        pass # TODO Rooms load

    def unload(self):
        pass

rooms = {
    "start": Room("start", ["left"], "start.idk"),
    "left": Room("left", ["start"], "left.idk")
}