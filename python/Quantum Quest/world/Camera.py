import numpy as np

def defaultSoftSpeed(distance: np.ndarray, speed: float, scale) -> np.ndarray:
    return distance * (1 - np.power(0.01 / scale, speed))

class Camera:
    def __init__(self, scale, target, softBorder: np.ndarray, hardBorder: np.ndarray, softSpeed = defaultSoftSpeed) -> None:
        """
        If the target is outside the softborder slowly move towards the target.
        If the target is outside the hardborder snapp to the target.
        """
        self.scale = scale
        self.target = target
        self.softBorder = softBorder
        self.hardBorder = hardBorder
        self.softSpeed = softSpeed

        self.position = target.getPosition()*self.scale

    def setTarget(self, target) -> None:
        self.target = target

    def getTarget(self):
        return self.target
    
    def getPosition(self) -> np.ndarray:
        return self.position
    
    def topLeft(self) -> np.ndarray:
        return self.hardBorder[0]

    def setSoftBorder(self, softBorder: np.ndarray) -> None:
        self.softBorder = softBorder

    def getSoftBorder(self) -> np.ndarray:
        return self.softBorder

    def setHardBorder(self, hardBorder: np.ndarray) -> None:
        self.hardBorder = hardBorder

    def getHardBorder(self) -> np.ndarray:
        return self.hardBorder

    def setSoftSpeed(self, softSpeed) -> None:
        self.softSpeed = softSpeed

    def move(self, distance: np.ndarray) -> None:
        self.position += distance
        self.softBorder += distance
        self.hardBorder += distance

    def tick(self, speed: float) -> None:
        # if target is contained within soft border
        distanceSoftBorder = self.target.hitbox.distanceToContained(self.getSoftBorder())
        distanceHardBorder = (self.target.hitbox).distanceToContained(self.getHardBorder())
        if np.all(distanceSoftBorder == 0):
            return
        elif np.all(distanceHardBorder == 0):
            self.move(self.softSpeed(distanceSoftBorder, speed, self.scale))
        else:
            self.move(distanceHardBorder)