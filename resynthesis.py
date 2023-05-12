# import libraries
import argparse
import os
import numpy as np
from scipy.io.wavfile import write


parser = argparse.ArgumentParser()
parser.add_argument("listsfile", help="Name of the lists file with the extension")
args = parser.parse_args()

listsfile_no_ext = os.path.splitext(args.listsfile)[0]

with open(args.listsfile) as f:
    frequencies = []
    amplitudes = []
    bandwidths = []
    for line in f:
        if listsfile_no_ext+"_frequencies" in line:
            frequencies = [float(x) for x in f.readline().split(", ")]
        elif listsfile_no_ext+"_amplitudes" in line:
            amplitudes = [float(x) for x in f.readline().split(", ")]
        elif listsfile_no_ext+"_bandwidths" in line:
            bandwidths = float(line.split("=")[1])


# -------- RESYNTHESIS DATA SAMPLES

duration = 10  # seconds
samplerate = 44100 # SR (per seconds)
num_samples = samplerate * duration # samples

# phase step increment
step = duration / num_samples

# start from 0
signal = np.zeros(num_samples)

# make a sinusoid for every elements of the lists
for freq, amp in zip(frequencies, amplitudes):
    phase = 2 * np.pi * freq * np.arange(num_samples) * step
    signal += amp * np.sin(phase)

# normalize between -1 +1
signal /= np.max(np.abs(signal))

# create or open the file in write mode
with open("resynthesisdata.txt", "w") as f:
    # write each sample to the file
    for sample in signal:
        f.write('{:.8f}\n'.format(sample))


# -------- RESYNTHESIS WAV

# read in the data from the text file
data = np.loadtxt('resynthesisdata.txt')

# set the sample rate to 44100 Hz
sample_rate = 44100

# scale the data to the range [-1, 1]
scaled_data = np.int16(data/np.max(np.abs(data)) * 32767)

# write the data to a .wav file
write('resynthesis.wav', sample_rate, scaled_data)