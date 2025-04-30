from time import perf_counter

alias PI: Float64 = 3.14159265358979323846
alias SOLAR_MASS: Float64 = 4 * PI * PI
alias DAYS_PER_YEAR: Float64 = 365.24
alias vec3 = SIMD[DType.float64, 4]

@value
struct Planet:
    var position: vec3
    var velocity: vec3
    var mass: Float64

    fn __init__(out self,
                read position: vec3,
                read velocity: vec3,
                read mass: Float64):
        self.position = position
        self.velocity = velocity
        self.mass = mass

alias Sun = Planet(
    0,
    0,
    SOLAR_MASS,
)
alias Jupiter = Planet(
    vec3(
        4.84143144246472090e00,
        -1.16032004402742839e00,
        -1.03622044471123109e-01,
        0,
    ),
    vec3(
        1.66007664274403694e-03 * DAYS_PER_YEAR,
        7.69901118419740425e-03 * DAYS_PER_YEAR,
        -6.90460016972063023e-05 * DAYS_PER_YEAR,
        0,
    ),
    9.54791938424326609e-04 * SOLAR_MASS,
)
alias Saturn = Planet(
    vec3(
        8.34336671824457987e00,
        4.12479856412430479e00,
        -4.03523417114321381e-01,
        0,
    ),
    vec3(
        -2.76742510726862411e-03 * DAYS_PER_YEAR,
        4.99852801234917238e-03 * DAYS_PER_YEAR,
        2.30417297573763929e-05 * DAYS_PER_YEAR,
        0,
    ),
    2.85885980666130812e-04 * SOLAR_MASS,
)
alias Uranus = Planet(
    vec3(
        1.28943695621391310e01,
        -1.51111514016986312e01,
        -2.23307578892655734e-01,
        0,
    ),
    vec3(
        2.96460137564761618e-03 * DAYS_PER_YEAR,
        2.37847173959480950e-03 * DAYS_PER_YEAR,
        -2.96589568540237556e-05 * DAYS_PER_YEAR,
        0,
    ),
    4.36624404335156298e-05 * SOLAR_MASS,
)
alias Neptune = Planet(
    vec3(
        1.53796971148509165e01,
        -2.59193146099879641e01,
        1.79258772950371181e-01,
        0,
    ),
    vec3(
        2.68067772490389322e-03 * DAYS_PER_YEAR,
        1.62824170038242295e-03 * DAYS_PER_YEAR,
        -9.51592254519715870e-05 * DAYS_PER_YEAR,
        0,
    ),
    5.15138902046611451e-05 * SOLAR_MASS,
)

alias INITIAL_SYSTEM = List[Planet](Sun, Jupiter, Saturn, Uranus, Neptune)
alias nBodies: Int = len(INITIAL_SYSTEM)

fn advance(read dt: Float64, 
           read n: Int,
           mut bodies: List[Planet]):
    for _ in range(n):
        for i in range(nBodies - 1):
            var body_i: Planet = bodies[i]
            for j in range(i + 1, nBodies):
                var body_j: Planet = bodies[j]
                var dx: vec3 = body_i.position - body_j.position
                var mag: Float64 = dt * (dx * dx).reduce_add() ** -1.5

                body_i.velocity -= dx * body_j.mass * mag
                body_j.velocity += dx * body_i.mass * mag

                bodies[i] = body_i
                bodies[j] = body_j
        for body in bodies:
            body[].position += body[].velocity * dt

fn energy(bodies: List[Planet]) -> Float64:
    var e: Float64 = 0.0

    for i in range(nBodies):
        e += 0.5 * bodies[i].mass * (bodies[i].velocity * bodies[i].velocity).reduce_add() # Kinetic energy
        for j in range(i + 1, nBodies):
            var dx: vec3 = bodies[i].position - bodies[j].position
            var dist: Float64 = (dx * dx).reduce_add() ** 0.5
            e -= (bodies[i].mass * bodies[j].mass) / dist # Potential energy
    return e

fn offset_momentum(mut bodies: List[Planet]):
    var p: vec3 = vec3()
    
    for body in bodies:
        p += body[].velocity * body[].mass

    var body: Planet = bodies[0]
    body.velocity = -p / body.mass

    bodies[0] = body

fn main():
    var n: Int = 50000000
    var dt: Float64 = 0.01

    var system: List[Planet] = INITIAL_SYSTEM

    offset_momentum(system)
    var initial_energy: Float64 = energy(system)

    print("Initial energy: ", initial_energy)

    print("Advancing simulation...")

    var start: Float64 = perf_counter()
    advance(dt, n, system)
    var end: Float64 = perf_counter()
    
    print("Simulation time: ", end - start, " seconds")
    
    var final_energy: Float64 = energy(system)
    print("Final energy: ", final_energy)
    print("Energy difference: ", final_energy - initial_energy)