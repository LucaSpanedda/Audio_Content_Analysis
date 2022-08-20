import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt

# Plot

# name output
xcoor = input("Enter your x coordinates (without txt extension):")
xplt = np.loadtxt(xcoor+".txt")

# numero di grafici verticali, numero di finestre orizzontali, numero progressivo
plt.subplot(1,1,1)
plt.grid()
plt.plot(xplt)
plt.ylabel('[Wave]')
plt.xlabel('[Samples]')

# nomina output
nomeplot = xcoor+"-Wave.png"

# salva output
plt.savefig(nomeplot)