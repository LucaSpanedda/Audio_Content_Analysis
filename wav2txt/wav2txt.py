# librerie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# leggiamo un file audio mono importandolo da terminale
audiofile = input("Enter your file name (without extension):")

# leggiamo il file audio e ne stampiamo la durata
[fs, x] = read(audiofile+".wav")
print("SR: ",fs,"\ndimensione del file audio in campioni: ", np.size(x))

# normalizziamo il file audio(a 0 dB)
# dividendo il file per l'assoluto del suo massimo
x = x/np.max(abs(x))

# salva file audio su testo
np.savetxt(audiofile+".txt", x, fmt='%1.8f')