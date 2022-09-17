# Phase Space 3D Plot

import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt

# Plot

xplt = np.loadtxt("x.txt")
yplt = np.loadtxt("y.txt")
zplt = np.loadtxt("z.txt")

# name output
nomeplot = "XYZ-phase-space"


fig = plt.figure()
ax = Axes3D(fig) 

# Hide grid lines
ax.grid(False)
# Hide axes grid
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
# background color
# Set the background color of the panes
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

ax.plot(xplt, yplt, zplt, color='black', alpha=1.0, linewidth=0.4)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Phase Space")

# save output
plt.savefig(nomeplot+".pdf")
