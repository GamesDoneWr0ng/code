import numpy as np
from time import time
from math import pi

SOLAR_MASS = 4 * pi * pi
DAYS_PER_YEAR = 365.24
# The bodies in the solar system
bodies = np.array([
    # x, y, z, vx, vy, vz, mass
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SOLAR_MASS], # sun
    [4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01,
     1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR,
     -6.90460016972063023e-05 * DAYS_PER_YEAR, 9.54791928888218753e-04 * SOLAR_MASS], # jupiter
    [8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01,
     -2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR,
     -2.30417297573763929e-05 * DAYS_PER_YEAR, 2.85885980666130966e-04 * SOLAR_MASS], # saturn
    [1.28943695621391310e+01, -1.51111514016956024e+01, -2.23307578813924624e-01,
     2.96460164571956077e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR,
     -2.96589568540237334e-05 * DAYS_PER_YEAR, 4.36624405750199451e-05 * SOLAR_MASS], # uranus
    [1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01,
     2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62832187412505255e-03 * DAYS_PER_YEAR,
     -9.51592254519715870e-05 * DAYS_PER_YEAR, 5.15138902046202247e-05 * SOLAR_MASS], # neptune
])

def advance(dt, n, bodies):
    """
    Advance the simulation by n steps.
    """
    for _ in range(n):
        for i in range(len(bodies) - 1):
            for j in range(i + 1, len(bodies)):
                dx = bodies[j, :3] - bodies[i, :3]
                dist = np.linalg.norm(dx)
                force = (bodies[i, 6] * bodies[j, 6]) / (dist ** 2)
                bodies[i, 3:6] += force * dx / bodies[i, 6] * dt
                bodies[j, 3:6] -= force * dx / bodies[j, 6] * dt
        bodies[:, :3] += bodies[:, 3:6] * dt
    return bodies

def energy(bodies):
    """
    Calculate the total energy of the system.
    """
    e = 0.0
    for i in range(len(bodies)):
        e += 0.5 * bodies[i, 6] * np.linalg.norm(bodies[i, 3:6]) ** 2 # kinetic energy
        for j in range(i + 1, len(bodies)):
            dx = bodies[j, :3] - bodies[i, :3]
            dist = np.linalg.norm(dx)
            e -= (bodies[i, 6] * bodies[j, 6]) / dist # potential energy
    return e

def main(bodies = bodies):
    """
    Main function to run the simulation.
    """
    n = 50000000
    dt = 0.01
    print("Initial positions:")
    print(bodies[:, :3])
    initial_energy = energy(bodies)
    print("Initial total energy:", initial_energy)
    print("Advancing the simulation...")
    start_time = time()
    bodies = advance(dt, n, bodies)
    end_time = time()
    print("Simulation time:", end_time - start_time, "seconds")
    print("Final positions:")
    print(bodies[:, :3])
    final_energy = energy(bodies)
    print("Total energy:", final_energy)
    print("Energy difference:", final_energy - initial_energy)

if __name__ == "__main__":
    main()