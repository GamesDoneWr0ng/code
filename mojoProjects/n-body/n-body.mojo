from time import perf_counter
from python import Python, PythonObject

alias Float = Float64
alias vec3 = SIMD[DType.float64, 4]

alias PI: Float = 3.14159265358979323846
alias SOLAR_MASS: Float = 4 * PI * PI
alias DAYS_PER_YEAR: Float = 365.2422

@value
struct Planet:
    var position: vec3
    var velocity: vec3
    var mass: Float

    fn __init__(out self,
                read position: vec3,
                read velocity: vec3,
                read mass: Float):
        self.position = position
        self.velocity = velocity
        self.mass = mass

fn init_planets(read date: String) -> List[Planet]:
    try:
        var jplhorizons = Python.import_module("astroquery.jplhorizons")
        var astropy = Python.import_module("astropy")
        
        var epoch   = astropy.time.Time(date, format="iso")
        var sun     = jplhorizons.Horizons(id="10",  location='@sun', epochs=epoch.jd).vectors()
        var earth   = jplhorizons.Horizons(id="399", location='@sun', epochs=epoch.jd).vectors()
        var moon    = jplhorizons.Horizons(id="301", location='@sun', epochs=epoch.jd).vectors()
        var mercury = jplhorizons.Horizons(id="199", location='@sun', epochs=epoch.jd).vectors()
        var venus   = jplhorizons.Horizons(id="299", location='@sun', epochs=epoch.jd).vectors()
        var mars    = jplhorizons.Horizons(id="499", location='@sun', epochs=epoch.jd).vectors()
        var jupiter = jplhorizons.Horizons(id="599", location='@sun', epochs=epoch.jd).vectors()
        var saturn  = jplhorizons.Horizons(id="699", location='@sun', epochs=epoch.jd).vectors()
        var uranus  = jplhorizons.Horizons(id="799", location='@sun', epochs=epoch.jd).vectors()
        var neptune = jplhorizons.Horizons(id="899", location='@sun', epochs=epoch.jd).vectors()
        return List[Planet](
            Planet(
                vec3(Float(Float64(sun["x"])),  Float(Float64(sun["y"])),  Float(Float64(sun["z"])),  0),
                vec3(Float(Float64(sun["vx"])), Float(Float64(sun["vy"])), Float(Float64(sun["vz"])), 0)*DAYS_PER_YEAR,
                SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(earth["x"])),  Float(Float64(earth["y"])),  Float(Float64(earth["z"])),  0),
                vec3(Float(Float64(earth["vx"])), Float(Float64(earth["vy"])), Float(Float64(earth["vz"])), 0)*DAYS_PER_YEAR,
                3e-6*SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(moon["x"])),  Float(Float64(moon["y"])),  Float(Float64(moon["z"])),  0),
                vec3(Float(Float64(moon["vx"])), Float(Float64(moon["vy"])), Float(Float64(moon["vz"])), 0)*DAYS_PER_YEAR,
                3.69e-8*SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(mercury["x"])),  Float(Float64(mercury["y"])),  Float(Float64(mercury["z"])),  0),
                vec3(Float(Float64(mercury["vx"])), Float(Float64(mercury["vy"])), Float(Float64(mercury["vz"])), 0)*DAYS_PER_YEAR,
                1.652e-7*SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(venus["x"])),  Float(Float64(venus["y"])),  Float(Float64(venus["z"])),  0),
                vec3(Float(Float64(venus["vx"])), Float(Float64(venus["vy"])), Float(Float64(venus["vz"])), 0)*DAYS_PER_YEAR,
                2.447e-6*SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(mars["x"])),  Float(Float64(mars["y"])),  Float(Float64(mars["z"])),  0),
                vec3(Float(Float64(mars["vx"])), Float(Float64(mars["vy"])), Float(Float64(mars["vz"])), 0)*DAYS_PER_YEAR,
                3.213e-7*SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(jupiter["x"])),  Float(Float64(jupiter["y"])),  Float(Float64(jupiter["z"])),  0),
                vec3(Float(Float64(jupiter["vx"])), Float(Float64(jupiter["vy"])), Float(Float64(jupiter["vz"])), 0)*DAYS_PER_YEAR,
                9.54588e-4 * SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(saturn["x"])),  Float(Float64(saturn["y"])),  Float(Float64(saturn["z"])),  0),
                vec3(Float(Float64(saturn["vx"])), Float(Float64(saturn["vy"])), Float(Float64(saturn["vz"])), 0)*DAYS_PER_YEAR,
                2.857e-4 * SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(uranus["x"])),  Float(Float64(uranus["y"])),  Float(Float64(uranus["z"])),  0),
                vec3(Float(Float64(uranus["vx"])), Float(Float64(uranus["vy"])), Float(Float64(uranus["vz"])), 0)*DAYS_PER_YEAR,
                4.365e-5 * SOLAR_MASS,
            ),
            Planet(
                vec3(Float(Float64(neptune["x"])),  Float(Float64(neptune["y"])),  Float(Float64(neptune["z"])),  0),
                vec3(Float(Float64(neptune["vx"])), Float(Float64(neptune["vy"])), Float(Float64(neptune["vz"])), 0)*DAYS_PER_YEAR,
                5.149e-5 * SOLAR_MASS,
            )
        )
    except:
        print("Error initializing planets. Ensure astroquery and astropy are installed.")
        return List[Planet]()

alias nBodies: Int = 10

fn f(read y: List[Planet]) -> List[Tuple[vec3, vec3]]:
    var result: List[Tuple[vec3, vec3]] = List[Tuple[vec3, vec3]]()
    for _ in range(nBodies):
        result.append((vec3(), vec3()))

    for i in range(nBodies):
        result[i][0] = y[i].velocity
        for j in range(i + 1, nBodies):
            var dx: vec3 = y[i].position - y[j].position
            var mag: Float = (dx * dx).reduce_add() ** -1.5
            
            result[i] = (result[i][0], result[i][1] - dx * y[j].mass * mag)
            result[j] = (result[j][0], result[j][1] + dx * y[i].mass * mag)

    return result

fn nextState(read bodies: List[Planet], 
         read k: List[Tuple[vec3, vec3]],
         read dt: Float) -> List[Planet]:
    var result: List[Planet] = List[Planet]()
    for i in range(nBodies):
        var body: Planet = bodies[i]
        var new_position: vec3 = body.position + k[i][0] * dt
        var new_velocity: vec3 = body.velocity + k[i][1] * dt
        result.append(Planet(new_position, new_velocity, body.mass))
    return result

fn advance(read dt: Float, 
           mut bodies: List[Planet]):
    # RK4 integration
    var k1: List[Tuple[vec3, vec3]] = f(bodies)
    var k2: List[Tuple[vec3, vec3]] = f(nextState(bodies, k1, dt * 0.5))
    var k3: List[Tuple[vec3, vec3]] = f(nextState(bodies, k2, dt * 0.5))
    var k4: List[Tuple[vec3, vec3]] = f(nextState(bodies, k3, dt))

    for i in range(nBodies):
        bodies[i].position += (k1[i][0] + 2 * k2[i][0] + 2 * k3[i][0] + k4[i][0]) * dt / 6
        bodies[i].velocity += (k1[i][1] + 2 * k2[i][1] + 2 * k3[i][1] + k4[i][1]) * dt / 6

fn energy(bodies: List[Planet]) -> Float:
    var e: Float = 0.0

    for i in range(nBodies):
        e += 0.5 * bodies[i].mass * (bodies[i].velocity * bodies[i].velocity).reduce_add() # Kinetic energy
        for j in range(i + 1, nBodies):
            var dx: vec3 = bodies[i].position - bodies[j].position
            var dist: Float = (dx * dx).reduce_add() ** 0.5
            e -= (bodies[i].mass * bodies[j].mass) / dist # Potential energy
    return e

fn offset_momentum(mut bodies: List[Planet]):
    var p: vec3 = vec3()
    
    for body in bodies:
        p += body[].velocity * body[].mass

    var body: Planet = bodies[0]
    body.velocity = -p / body.mass

    bodies[0] = body

fn referenceFrame(mut bodies: List[Planet]):
    var reference: Planet = bodies[0]
    for i in range(nBodies):
        bodies[i].position -= reference.position
        bodies[i].velocity -= reference.velocity

alias names: List[String] = List[String]("Sun", "Earth", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

fn logPlanets(read bodies: List[Planet],
              mut  log: List[List[vec3]]):
    for i in range(nBodies):
        var body: Planet = bodies[i]
        log[i].append(body.position)

fn prepareLog(read log: List[List[vec3]]) raises -> PythonObject:
    var res: PythonObject = Python.evaluate("[[],[],[]]")
    for i in range(len(log)):
        var planetX: PythonObject = Python.list()
        var planetY: PythonObject = Python.list()
        var planetZ: PythonObject = Python.list()
        for j in range(len(log[i])):
            planetX.append(log[i][j][0])
            planetY.append(log[i][j][1])
            planetZ.append(log[i][j][2])
        res[0].append(planetX)
        res[1].append(planetY)
        res[2].append(planetZ)
    return res

fn main():
    var years: Int = 165
    var n: Int = 365*years
    var dt: Float = years / n # in years

    var system: List[Planet] = init_planets("2022-05-05 00:00:00")

    # for i in range(nBodies):
    #     print("Planet ", i, ": ", system[i].position, system[i].velocity)

#    offset_momentum(system)
    referenceFrame(system)
#    var initial_energy: Float = energy(system)

#    print("Initial energy: ", initial_energy)

    var log: List[List[vec3]] = List[List[vec3]]()
    for _ in range(nBodies):
        log.append(List[vec3]())

    print("Advancing simulation...")

    var start: Float64 = perf_counter()
    for _ in range(n):
        advance(dt, system)
        logPlanets(system, log)
    var end: Float64 = perf_counter()
    
    print("Simulation time: ", end - start, " seconds")
    
    #var final_energy: Float = energy(system)
    #print("Final energy: ", final_energy)
    #print("Energy difference: ", final_energy - initial_energy)

    # var expected: List[Planet] = init_planets("2023-05-05 00:00:00")
    # for i in range(nBodies):
    #     print("Planet ", i, ": ", system[i].position, system[i].velocity)
    #     print("Expected Planet ", i, ": ", expected[i].position, expected[i].velocity)
    #     print("Difference: ", system[i].position - expected[i].position, system[i].velocity - expected[i].velocity)
    #     print()
    
    var py_module = """
def render(data):
    trail_length=150
    print("Rendering animation...")
    # Validate input
    assert len(data) == 3, "Data must contain [x, y, z] components"
    assert len(data[0]) == len(data[1]) == len(data[2]), "Coordinate lists must have equal numbers of bodies"

    from matplotlib import pyplot as plt
    from matplotlib.animation import FuncAnimation
    import numpy as np
    
    n_planets = len(data[0])
    n_frames = len(data[0][0])
    
    # Set default visual parameters
    colors = ['gold', 'blue', 'black',    'gray',   'red', "orange",   'brown',  'yellow', 'green', 'blue'][:n_planets]
    labels = ["Sun", "Earth",  "Moon", "Mercury", "Venus",   "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"][:n_planets]
    sizes = [12, 6, 4, 4, 4, 6, 8, 7, 6, 6][:n_planets]
    
    # Setup figure
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Auto-scale axes based on data extremes
    all_coords = np.concatenate([np.array(data[i]) for i in range(3)])
    max_extent = np.max(np.abs(all_coords)) * 1.2
    ax.set_xlim(-max_extent, max_extent)
    ax.set_ylim(-max_extent, max_extent)
    ax.set_zlim(-max_extent, max_extent)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(True)
    ax.set_title('n-body simulation')

    # Create plot objects for each body
    lines = []
    for i in range(n_planets):
        line, = ax.plot([], [], [], 
                       marker='o',
                       markersize=sizes[i],
                       color=colors[i],
                       lw=1,
                       markevery=[-1],
                       label=labels[i])
        lines.append(line)
    ax.legend()

    # Animation functions
    def init():
        for line in lines:
            line.set_data([], [])
            line.set_3d_properties([])
        return lines

    def update(frame):
        start = max(0, frame - trail_length)
        
        for i in range(n_planets):
            x = data[0][i][start:frame+1]
            y = data[1][i][start:frame+1]
            z = data[2][i][start:frame+1]
            
            lines[i].set_data(x, y)
            lines[i].set_3d_properties(z)
            
        return lines

    # Create and show animation
    ani = FuncAnimation(
        fig,
        update,
        frames=n_frames,
        init_func=init,
        blit=False,
        interval=20
    )
    
    plt.show()
    """
    try:
        var pyRender = Python.evaluate(py_module, file=True, name="pyRender")
        pyRender.render(prepareLog(log))
    except:
        print("Error rendering.")