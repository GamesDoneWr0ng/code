from util.math.Hitbox import Hitbox
from world.objects.Object import Object

class Trigger(Object):
    def __init__(self, hitbox: Hitbox, room, hasCollision: bool = True, solid = False) -> None:
        super().__init__(hitbox, room, hasCollision)
        self.entities: dict = {}
        self.solid: bool = solid

    def isTrigger(self) -> bool:
        return True
    
    def onCollide(self, entity):
        if entity.getId() in self.entities:
            self.onStay(entity)
            return self.solid
            
        self.onEnter(entity)
        self.entities[entity.getId()] = entity
        return self.solid

    def onEnter(self, entity):
        pass

    def onExit(self, entity):
        pass

    def onStay(self, entity):
        pass

    def tick(self):
        # Create a copy of the keys to avoid modifying dictionary size during iteration
        for entityId in list(self.entities.keys()):
            entity = self.entities[entityId]
            collision, _, _ = self.hitbox.checkCollision(entity.getHitbox())
            if not collision:
                self.onExit(entity)
                del self.entities[entity.getId()]