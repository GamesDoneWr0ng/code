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

"""if __name__ == "__main__":
    
    import numpy as np
    n_frames = 200
    t = np.linspace(0, 4*np.pi, n_frames)

    # Sun (stationary at origin)
    sun_x = np.zeros(n_frames)
    sun_y = np.zeros(n_frames)
    sun_z = np.zeros(n_frames)

    # Earth's orbit (circular in xy-plane, z=0)
    earth_radius = 1.0
    earth_x = earth_radius * np.cos(t)
    earth_y = earth_radius * np.sin(t)
    earth_z = np.zeros(n_frames)

    # Moon's orbit (3D example: elliptical orbit with z-variation)
    moon_radius = 0.2
    moon_x = earth_x + moon_radius * np.cos(12 * t)
    moon_y = earth_y + moon_radius * np.sin(12 * t)
    moon_z = 0.1 * np.sin(8 * t)  # Add some vertical motion

    render(((sun_x, earth_x, moon_x), (sun_y, earth_y, moon_y), (sun_z, earth_z, moon_z)))"""