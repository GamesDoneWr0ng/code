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