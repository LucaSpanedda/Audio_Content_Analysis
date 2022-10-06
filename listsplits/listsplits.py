import sys
import numpy as np

# divide a text list in N parts
xcoor = input("Enter your txt file with samples (without txt extension):")
listA = np.loadtxt(xcoor+".txt")

# numero di splits
splits = np.array_split(listA, 200)

# Apre tre file di testo per i valori di X
f = open(xcoor+"-splits"+".txt", "w")

for array in splits:
    # print dei risultati in file X
    loopsplits = list(array)
    f.write(str(loopsplits))
    f.write('\n')

f.close()
