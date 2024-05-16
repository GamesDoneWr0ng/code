from world.objects.Playform import Platform
from util.math.Hitbox import Polygon
from entities.TempEntity import TempEntity
from world.objects.Transition import Transition
from entities.RemovalReason import RemovalReason
from entities.PlayerEntity import PlayerEntity
from world.objects.Object import Object
from entities.Entity import Entity
from entities import EntityType
import numpy as np
import json

class Room:
    def __init__(self, dataFile: str, world) -> None:
        self.world = world
        self.player: PlayerEntity = None

        self.dataFile: str = dataFile
        with open(self.dataFile, 'r') as file:
            data = json.load(file)

        self.id: str = data["id"]
        self.neighbours: list[str] = data["neighbours"]

        self.objects:  list[Object] = []
        for object in data["objects"]:
            match object["type"]:
                case "Platform":
                    #world.rooms["start"].addObject(Platform(Polygon(np.array([[-5, 3], [-5, 4], [11, 4], [11, 3]])), world.rooms["start"]))
                    self.addObject(Platform(Polygon(np.array(object["args"]["hitbox"])), self))
                case "Transition":
                    self.addObject(Transition(Polygon(np.array(object["args"]["hitbox"])), self, object["args"]["connected"], np.array(object["args"]["direction"])))

        self.entities: list[Entity] = []
        for entity in data["entities"]:
            match entity["type"]:
                case "TempEntity":
                    self.addEntity(TempEntity(self))

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
        self.entities.remove(entity)
        entity.remove(reason)

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
        for entity in self.entities:
            entity.remove(RemovalReason.UNLOAD)