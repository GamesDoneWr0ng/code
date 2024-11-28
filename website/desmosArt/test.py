import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def dft(points):
    """Compute the Discrete Fourier Transform of a list of points."""
    n = len(points)
    fourier_coeffs = []
    for k in range(n):
        coeff = sum(points[j] * np.exp(-2j * np.pi * k * j / n) for j in range(n)) / n
        fourier_coeffs.append(coeff)
    return fourier_coeffs

def harmonic_circles(points, num_harmonics=10, num_frames=500):
    """Visualize Fourier Series Harmonic Circles for a list of points."""
    points = np.array(points, dtype=complex)
    n = len(points)
    fourier_coeffs = dft(points)

    # Sort coefficients by magnitude
    harmonics = sorted(
        ((np.abs(c), k, c) for k, c in enumerate(fourier_coeffs)),
        key=lambda x: x[0],
        reverse=True
    )[:num_harmonics]

    # Generate the animation
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set_xlim(points.real.min() - 1, points.real.max() + 1)
    ax.set_ylim(points.imag.min() - 1, points.imag.max() + 1)
    
    circle_lines = [plt.Circle((0, 0), radius=0, fill=False, color="gray") for _ in harmonics]
    for circle in circle_lines:
        ax.add_artist(circle)
    trajectory_line, = ax.plot([], [], 'r-', lw=1)
    points_scatter = ax.scatter(points.real, points.imag, s=5, c='blue')

    trajectory = []

    def update(frame):
        nonlocal trajectory
        x, y = 0, 0
        for i, (_, k, coeff) in enumerate(harmonics):
            freq = k
            radius = np.abs(coeff)
            phase = np.angle(coeff)
            x += radius * np.cos(2 * np.pi * freq * frame / num_frames + phase)
            y += radius * np.sin(2 * np.pi * freq * frame / num_frames + phase)
            circle_lines[i].center = (x, y)
            circle_lines[i].radius = radius

        trajectory.append((x, y))
        trajectory = trajectory[-n:]
        trajectory_line.set_data(*zip(*trajectory))

        return trajectory_line, *circle_lines

    ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)
    plt.show()

# Example usage:
# Define some points that follow a path (e.g., a circle)
t = np.linspace(0, 2 * np.pi, 100)
points = np.exp(1j * t)  # A simple circle

# Visualize the harmonic circles
harmonic_circles(points, num_harmonics=10, num_frames=500)
