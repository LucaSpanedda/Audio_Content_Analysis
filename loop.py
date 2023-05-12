from scipy.io import wavfile
import numpy as np
import playsound
from multiprocessing import Process
import time

# Read in the audio file
rate, data = wavfile.read('audio_file.wav')

# Apply the Hann window
window = np.hanning(len(data))
data_windowed = window * data

# Apply a scaling factor to prevent clipping
data_windowed *= 0.5 / np.max(np.abs(data_windowed))

# Write the windowed audio to a temporary file
wavfile.write('audio_file_windowed.wav', rate, data_windowed)

def play_audio(delay):
    while True:
        playsound.playsound('audio_file_windowed.wav', True)

if __name__ == '__main__':
    p1 = Process(target=play_audio, args=(0,))
    p2 = Process(target=play_audio, args=(0,))
    p1.start()
    time.sleep(len(data_windowed) / rate / 2)
    p2.start()