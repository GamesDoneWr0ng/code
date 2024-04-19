from python import Python 

struct Spiller:
    var pos: SIMD[DType.float32, 2]
    var speed: Int
    var radius: Int
    var color: Tuple[UInt8,UInt8,UInt8]
    
    def __init__(
            inout self, 
            owned pos: SIMD[DType.float32, 2], 
            owned speed: Int,
            owned radius: Int,
            owned color: Tuple[UInt8,UInt8,UInt8]
        ):
        self.pos = pos
        self.speed = speed
        self.radius = radius
        self.color = color

    def draw(inout self, borrowed pg: PythonObject, inout screen: PythonObject):
        pg.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.radius)

    def move(inout self, borrowed pg: PythonObject):
        var keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.pos[1] -= self.speed

fn main() raises:
    var pg = Python.import_module("pygame")
    pg.init()

    var SIZE = SIMD[DType.float32, 2](800,600)
    var screen = pg.display.set_mode((SIZE[0], SIZE[1]))

    var spiller = Spiller(SIZE/2, 1, 20, Tuple[UInt8,UInt8,UInt8](255,0,0))

    var running = True
    while running:
        screen.fill((0,0,0))
        spiller.draw(pg, screen)
        pg.display.flip()
