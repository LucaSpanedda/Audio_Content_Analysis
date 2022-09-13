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

ax.plot(xplt, yplt, zplt, color='g', alpha=0.7, linewidth=0.6)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Phase Space")

# save output
plt.savefig(nomeplot+".pdf")