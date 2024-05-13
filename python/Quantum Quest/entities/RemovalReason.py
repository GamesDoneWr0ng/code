class RemovalReason:
    def __init__(self, name: str, destroy: bool, save: bool):
        self.name = name
        self.destroy = destroy
        self.save = save

    def __eq__(self, other):
        if isinstance(other, RemovalReason):
            return self.name == other.name
        return False
    
    def should_destroy(self):
        """Should drop loot."""
        return self.destroy
 
    def should_save(self):
        """Save entity to be load back in again later."""
        return self.save

KILLED = RemovalReason("KILLED", True, False) # Killed
UNLOADED = RemovalReason("UNLOADED", False, True)
UNLOADED_WITH_PLAYER = RemovalReason("UNLOADED_WITH_PLAYER", False, False)
MOVED = RemovalReason("MOVED", False, False)