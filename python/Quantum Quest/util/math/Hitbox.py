import numpy as np

class Hitbox:
    def __init__(self, type: str) -> None:
        self.type = type

    def getType(self) -> str:
        return self.type

    def move(self, movement: np.ndarray):
        raise NotImplementedError
    
    def newMove(self, movement: np.ndarray):
        raise NotImplementedError
    
    def setPosition(self, position: np.ndarray):
        raise NotImplementedError

    def getPosition(self) -> np.ndarray:
        raise NotImplementedError

    def getMaxRadius(self) -> float:
        raise NotImplementedError
    
    def getMinRadius(self) -> float:
        raise NotImplementedError

    def checkCollision(self, other) -> tuple[bool, np.ndarray]:
        squaredDistance = np.sum((self.getPosition() - other.getPosition())**2)
        #if squaredDistance < (self.getMinRadius() + other.getMinRadius())**2: # doesent work since we dont know correction
        #    return True
        if squaredDistance > (self.getMaxRadius() + other.getMaxRadius())**2:
            return False
        else:
            return None
        
    def stretch(self, direction: np.ndarray) -> np.ndarray:
        raise NotImplementedError
    
    def getMax(self) -> np.ndarray:
        raise NotImplementedError
    
    def getMin(self) -> np.ndarray:
        raise NotImplementedError
    
    def distanceToContained(self, square: np.ndarray) -> np.ndarray:
        """Square has shape (2, 2) where square[0] is top left corner and square[1] is bottom left corner of a square.
        Returns the vector needed to move this hitbox so its fully contained within the square."""
        max = self.getMax()
        min = self.getMin()

        self_dx, self_dy = max - min
        square_dx, square_dy = square[1] - square[0]

        if self_dx > square_dx or self_dy > square_dy:
            return np.mean(square, axis=0) - self.position

        dmin = min - square[0]
        dmin[dmin>0] = 0
        dmax = max - square[1]
        dmax[dmax<0] = 0
        return dmin+dmax
    
    def touches(self, square: np.ndarray) -> bool:
        """Square has shape (2, 2) where square[0] is top left corner and square[1] is bottom left corner of a square.
        Returns if the Hitbox touches the square."""
        raise NotImplementedError


class Polygon(Hitbox):
    def __init__(self, points: np.ndarray) -> None:
        super().__init__("Polygon")
        self.points = points

        self.position = np.mean(self.points, axis=0)
        self.setRadiuses()

    def setRadiuses(self) -> None:
        distances = np.linalg.norm(self.points - self.position, axis=1)
        self.maxRadius = np.max(distances)
        self.minRadius = np.min(distances)

    def move(self, movement: np.ndarray) -> None:
        self.position += movement
        self.points += movement

    def newMove(self, movement: np.ndarray):
        return Polygon(self.points + movement)

    def setPosition(self,position: np.ndarray) -> None:
        lastPosition = self.position.copy()
        
        self.position = position

        diff = self.position - lastPosition
        self.points = self.points + diff

    def getPosition(self) -> np.ndarray:
        return self.position
    
    def getMaxRadius(self) -> float:
        return self.maxRadius
    
    def getMinRadius(self) -> float:
        return self.minRadius
    
    def findAxes(self) -> np.ndarray:
        # Calculate the edges of the polygon
        edges = np.roll(self.getPoints(), -1, axis=0) - self.getPoints()
        # Calculate the normals to the edges (perpendicular vectors)
        axes = np.array([-edges[:, 1], edges[:, 0]]).T
        return axes
    
    def projectPolygon(self, axis) -> np.ndarray:
        # Project the polygon onto the axis
        dots = np.dot(self.points, axis)
        return np.array([dots.min(), dots.max()])

    def satCollision(self, other) -> tuple[bool, np.ndarray, np.ndarray, np.ndarray]:
        # Combine the axes from both polygons
        axes = np.concatenate((self.findAxes(), other.findAxes()))

        corrections = np.zeros(axes.shape)

        for i, axis in enumerate(axes):
            # Normalize the axis
            axis = axis / np.linalg.norm(axis)

            # Project both polygons onto the axis
            projection1 = self.projectPolygon(axis)
            projection2 = other.projectPolygon(axis)

            # Check for overlap
            if projection1[1] < projection2[0] or projection2[1] < projection1[0]:
                return False, np.zeros(2), None # No overlap on this axis
            
            corrections[i] = axis * min(projection2[0]-projection1[1], projection2[1]-projection1[0], key=abs)

        index = np.argmin(np.sum(corrections**2, axis=1))
        return True, corrections[index], axes[index] / np.linalg.norm(axes[index]) # Overlap on all axes

    def stretch(self, direction: np.ndarray):
        if np.all(direction == 0):
            return self
        points = []
        dots = np.dot(self.findAxes(), direction)
        for point, dot, lastDot in zip(self.points, dots, np.roll(dots, -1)):
            if dot > 0 and lastDot > 0:
                points.append(point)
            elif dot > 0 and lastDot == 0:
                points.append(point)
            elif dot > 0 and lastDot < 0:
                points.append(point)
                points.append(point + direction)

            elif dot == 0 and lastDot > 0:
                points.append(point)
            elif dot == 0 and lastDot < 0:
                points.append(point + direction)

            elif dot < 0 and lastDot > 0:
                points.append(point)
                points.append(point + direction)
            elif dot < 0 and lastDot == 0:
                points.append(point + direction)
            elif dot < 0 and lastDot < 0:
                points.append(point + direction)

        return Polygon(points)
    
    def checkCollision(self, other) -> bool:
        preliminary = super().checkCollision(other)
        if preliminary is not None:
            return preliminary, np.zeros(2), None
        
        if other.getType() == "Polygon":
            return self.satCollision(other)
        
        elif other.getType() == "Circle":
            checkCollisionPolygonCircle(self,other)

    def getMax(self) -> np.ndarray:
        return np.max(self.points, axis=0)
    
    def getMin(self) -> np.ndarray:
        return np.min(self.points, axis=0)
    
    def touches(self, square: np.ndarray) -> bool:
        """Square has shape (2, 2) where square[0] is top left corner and square[1] is bottom left corner of a square.
        Returns if the Polygon touches the square."""
        return self.checkCollision(Polygon(np.array([[square[0,1], square[1,0]], square[1], [square[1,0], square[0,1]], square[0]])))[0]
    
    def getPoints(self) -> np.ndarray:
        return self.points
    

class Circle(Hitbox):
    def __init__(self, position: np.ndarray, radius: float) -> None:
        super().__init__("Circle")
        self.position = position
        self.radius = radius

    def move(self, movement: np.ndarray):
        self.position += movement

    def newMove(self, movement: np.ndarray):
        return Circle(self.position + movement, self.radius)

    def getPosition(self) -> np.ndarray:
        return self.position

    def getMaxRadius(self) -> float:
        return self.radius

    def getMinRadius(self) -> float:
        return self.radius

    def checkCollision(self, other: Hitbox) -> bool:
        preliminary = super().checkCollision(other)
        if preliminary is not None:
            return preliminary
        
        if other.getType() == "Polygon":
            return checkCollisionPolygonCircle(other,self)
        
    def getMax(self) -> np.ndarray:
        return self.position+self.radius
    
    def getMin(self) -> np.ndarray:
        return self.position-self.radius
    
    def touches(self, square: np.ndarray) -> bool:
        """Square has shape (2, 2) where square[0] is top left corner and square[1] is bottom left corner of a square.
        Returns if the Circle touches the square."""
        return np.any(np.logical_and(self.getMin() >= square[0], self.getMax() <= square[1]))

def checkCollisionPolygonCircle(polygon: Polygon, circle: Circle):
    return False # TODO collision polygon circle