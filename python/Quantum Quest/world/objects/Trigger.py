from ...util.math.Hitbox import Hitbox
from world.objects.Object import Object

class Trigger(Object):
    def __init__(self, hitbox: Hitbox, room, hasCollision: bool = True) -> None:
        super().__init__(hitbox, room, hasCollision)
        self.entities = {}

    def isTrigger(self) -> bool:
        return True
    
    def onCollide(self, entity):
        if entity.getId() in self.entities:
            self.onStay(entity)
            return
            
        self.onEnter(entity)
        self.entities[entity.getId()] = entity

    def onEnter(self, entity):
        pass

    def onExit(self, entity):
        pass

    def onStay(self, entity):
        pass

    def tick(self):
        for entity in self.entities.values():
            collision, _, _ = self.hitbox.checkCollision(entity.getHitbox())
            if not collision:
                self.onExit(entity)
                del self.entities[entity.getId()]