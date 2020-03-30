import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
from scipy import signal
import numpy as np
np.set_printoptions(threshold=1000)

rate, data = wav.read('Wildflower.wav')


sound = signal.resample(data,100000)

fft_out = fft(sound)

plt.plot(sound, np.abs(fft_out))
plt.show()