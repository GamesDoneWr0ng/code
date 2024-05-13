from world.objects.Object import Object
from util.math.Hitbox import Hitbox

class TickingObject(Object):
    def __init__(self, hitbox: Hitbox, room) -> None:
        super().__init__(hitbox, room)

    def isTicking(self) -> bool:
        return True

    def tick(self):
        raise NotImplementedError