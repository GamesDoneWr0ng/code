# %%
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import thin
import cv2
from scipy.fft import fft, fftfreq
from matplotlib.animation import FuncAnimation

img_path = "/Users/askborgen/Desktop/code/website/desmosArt/images/pikachu.jpeg"
binCutoff = 123
thinSteps = 6
plotprocess = True
nSample = 1500
nContours = 1
num_frames = 2000
num_harmonics = 3000

# %%
def img_to_outline(filepath):
    """image processing
    1) Load grayscale image
    2) Convert to binary array
    3) Skeletal thin
    4) Gaussian blur
    5) Canny edge detection
    """
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    binImg = np.array(img)
    binImg[binImg < binCutoff] = 1
    binImg[binImg > 1] = 0

    thinImg = thin(binImg, thinSteps)
    temp = np.zeros(thinImg.shape, dtype=np.uint8) # convert from binary array to 0-255 values
    temp[thinImg] = 255
    blurredImg = cv2.GaussianBlur(temp, (5,5), 1.4)
    edges = cv2.Canny(blurredImg, 50, 150)

    if plotprocess:
        fig, ((ax_orig, ax_bin, ax_thin), (ax_blur, ax_edge, _)) = plt.subplots(2, 3, figsize=(6, 15))
        ax_orig.imshow(img, cmap="gray")
        ax_bin.imshow(binImg, cmap="gray")
        ax_thin.imshow(thinImg, cmap="gray")
        ax_blur.imshow(blurredImg, cmap="gray")
        ax_edge.imshow(edges, cmap="gray")
        ax_orig.set_axis_off()
        ax_bin.set_axis_off()
        ax_thin.set_axis_off()
        ax_blur.set_axis_off()
        ax_edge.set_axis_off()
        fig.show()
        #plt.show()
    return edges

def img_to_svg(filepath):
    data = np.abs(img_to_outline(filepath))
    contours, _ = cv2.findContours(data, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    zeros = np.zeros(data.shape)
    #cv2.drawContours(zeros, contours, -1, 255, 3)
    
    #plt.imshow(zeros)
    #plt.show()
    points = []
    for i in sorted(contours, key=cv2.contourArea, reverse=True)[:nContours]:
        points.extend([pt[0] for pt in i])
    return np.array(points)

# %%
#path = path_to_array(sorted(img_to_svg(img_path)[2:], key=len, reverse=True)[:1])
#points = sample_path(path)
points = np.vstack(img_to_svg(img_path)) / cv2.imread(img_path).shape[0]
#points = np.vstack(points) / cv2.imread(img_path).shape[0]
points[:,1]*=-1

# %%
t = np.linspace(0, 2 * np.pi, len(points))
x = points[:,0]
y = points[:,1]

# Create a complex signal
#z = np.array([complex(x, -y) for x,y in points])
z = x + 1j * y

colors = np.arange(len(x))
plt.scatter(x,y, c=colors, cmap="viridis")

# %%
def harmonic_circles(points, num_harmonics=num_harmonics, num_frames=num_frames):
    """Visualize Fourier Series Harmonic Circles for a list of points."""
    points = np.array(points, dtype=complex)
    n = len(points)
    fourier_coeffs = fft(points) / n

    # Sort coefficients by magnitude
    harmonics = sorted(
        ((np.abs(c), k, np.angle(c)) for k, c in zip(np.round(fftfreq(len(fourier_coeffs))*n), fourier_coeffs)),
        key=lambda x: x[0],
        reverse=True
    )[:num_harmonics]

    # Print the data in JavaScript array format
    print("const data = [")
    for row in harmonics:
        print(f"  [{row[0]:.10g}, {row[1]:.10g}, {row[2]:.10g}],")
    print("];")

    # Generate the animation
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set_xlim(points.real.min() - 1, points.real.max() + 1)
    ax.set_ylim(points.imag.min() - 1, points.imag.max() + 1)
    
    #circle_lines = [plt.Circle((0, 0), radius=0, fill=False, color="gray") for _ in harmonics]
    #for circle in circle_lines:
    #    ax.add_artist(circle)

    trajectory_line, = ax.plot([], [], 'r-', lw=1)
    #points_scatter = ax.scatter(points.real, points.imag, s=5, c='blue')

    trajectory = []

    def update(frame):
        nonlocal trajectory
        x, y = 0, 0
        arrows = [ax.arrow(0,0,0,0,width=0,head_width=0,head_length=0) for i in harmonics]
        for i, (radius, freq, phase) in enumerate(harmonics):
            dx = radius * np.cos(2 * np.pi * freq * frame / num_frames + phase)
            dy = radius * np.sin(2 * np.pi * freq * frame / num_frames + phase)
            
            arrows[i]=(ax.arrow(x,y, dx, dy, head_width=0.005, head_length=0.01, width=0.001, color="blue"))
            
            x += dx
            y += dy

        trajectory.append((x, y))
        trajectory = trajectory[-n:]
        trajectory_line.set_data(*zip(*trajectory))

        return trajectory_line, *arrows[2:]

    ani = FuncAnimation(fig, update, frames=num_frames, interval=10, blit=True)
#    plt.show()

# %%
#plt.show()
harmonic_circles(z)
