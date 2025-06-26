import numpy as np
import pyvista as pv
from mayavi import mlab

# Generate your original grid and data (example)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
xx, yy = np.meshgrid(x, y, indexing='ij')
zz = np.sin(xx**2 + yy**2)  # Replace with your data

# Convert to PyVista StructuredGrid
grid = pv.StructuredGrid(xx, yy, zz)

# Extract surface as PolyData (triangular mesh)
mesh = grid.extract_surface().triangulate()

# Decimate: Reduce triangles by 70% in flat regions
decimated = mesh.decimate_pro(reduction=0.7, preserve_topology=True)

decimated.plot()