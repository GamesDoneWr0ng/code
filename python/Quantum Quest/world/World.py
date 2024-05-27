from world.Room import Room
from entities.Entity import Entity
from entities import RemovalReason
from entities.Player.PlayerEntity import PlayerEntity
from copy import deepcopy

class World:
    def __init__(self, screen) -> None:
        self.currentId = -1
        self.deltaTime = 1/60

        self.screen = screen 
        self.currentRoom: str = "start" # TODO rooms savefile
        self.rooms: dict[str, Room.Room] = {self.currentRoom: Room(f"/Users/askborgen/Desktop/code/python/Quantum Quest/world/rooms/{self.currentRoom}.json", self)}
        for room in self.rooms[self.currentRoom].getNeighbours():
            self.loadRoom(room)

        self.rooms["start"].addEntity(PlayerEntity(self.rooms["start"]))

        self.addedRooms = []
        self.removedRooms = []
        

    def getPlayer(self):
        return self.rooms[self.currentRoom].getPlayer()
    
    def getRoomById(self, id) -> Room:
        for room in self.rooms.values():
            if room.getId() == id:
                return room
        raise Exception(f"Room with id {id} not found")

    def move(self, roomFrom: str, roomTo: str, entity: Entity):
        if entity.isPlayer():
            for room in self.rooms[roomFrom].getNeighboursWithout(roomTo):
                self.removedRooms.append(room)
            for room in self.rooms[roomTo].getNeighboursWithout(roomFrom):
                self.addedRooms.append(room)
            self.currentRoom = roomTo

        self.getRoomById(roomTo).addEntity(entity)
        self.getRoomById(roomFrom).removeEntity(entity, RemovalReason.MOVED)
        entity.setRoom(self.rooms[roomTo])

    def tick(self, deltaTime: float):
        self.deltaTime = deltaTime
        for room in self.rooms.values():
            room.tick()

        # to avoid changing the dict while iterating
        for room in self.addedRooms:
            self.loadRoom(room)
        for room in self.removedRooms:
            self.rooms[room].unload()
            del self.rooms[room]
        self.addedRooms, self.removedRooms = [], []

    
    def render(self, camera, scale: float):
        for room in self.rooms.values():
            room.render(self.screen, camera, scale)

    def nextId(self) -> int:
        self.currentId += 1
        return self.currentId
    
    def getDeltaTime(self) -> float:
        return self.deltaTime
    
    def loadRoom(self, room: str):
        self.rooms[room] = Room(f"/Users/askborgen/Desktop/code/python/Quantum Quest/world/rooms/{room}.json", self)
        self.rooms[room].load()