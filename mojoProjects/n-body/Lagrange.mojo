from time import perf_counter
from python import Python

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
        
        var epoch = astropy.time.Time(date, format="iso")
        var sun   = jplhorizons.Horizons(id="10",  location='@sun', epochs=epoch.jd).vectors()
        var earth = jplhorizons.Horizons(id="399", location='@sun', epochs=epoch.jd).vectors()
        var moon  = jplhorizons.Horizons(id="301", location='@sun', epochs=epoch.jd).vectors()
        var mercury = jplhorizons.Horizons(id="199", location='@sun', epochs=epoch.jd).vectors()
        var venus = jplhorizons.Horizons(id="299", location='@sun', epochs=epoch.jd).vectors()
        var mars = jplhorizons.Horizons(id="499", location='@sun', epochs=epoch.jd).vectors()
        var jupiter = jplhorizons.Horizons(id="599", location='@sun', epochs=epoch.jd).vectors()
        var saturn = jplhorizons.Horizons(id="699", location='@sun', epochs=epoch.jd).vectors()
        var uranus = jplhorizons.Horizons(id="799", location='@sun', epochs=epoch.jd).vectors()
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