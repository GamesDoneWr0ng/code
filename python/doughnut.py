pi = 3.141592653589793
e = 2.718281828459045

# uses e^θi since e^θi = cos(θ) + i*sin(θ)
def sin(theta: float) -> float:
    return (e**(theta*1j)).imag
def cos(theta: float) -> float:
    return (e**(theta*1j)).real

class Doughnut:
    def __init__(self, radius: float, thickness: float, cameraPos: list, fov: float):
        self.radius: float = radius
        self.thickness: float = thickness
        self.cameraPos: list = cameraPos
        self.fov = fov
        self.rotation: list = [0, 0, 0]

    def rotate(self, angles):
        for i in range(3):
            self.rotation[i] += angles[i]

    def raycast(self, origin: list, direction: list) -> float:
        
        pass

    def draw(self, screenSize: tuple):
        result = ""
        for y in screenSize[1]:
            for x in screenSize[0]:
                direction = [
                    -cos(2 * x * self.fov / screenSize[0]) * self.cameraPos[0],
                    -sin(2 * y * self.fov / screenSize[1]) * self.cameraPos[1],
                    -sin(2 * x * self.fov / screenSize[0]) * self.cameraPos[2],
                ]

                if self.raycast(self.cameraPos, direction):
                    result += "#"
                else:
                    result += " "
            result += "\n"

        print(result)


screenSize = (50, 30)

doughnut = Doughnut(1, 0.3, [2,1,2], pi/2)