import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

# WAV dosyasını yükleyin
sample_rate, data = wavfile.read('melodi.wav')

# Sinyalin Fourier dönüşümünü hesaplayın
N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / sample_rate)

# Frekans spektrumunu görselleştirin
plt.plot(xf, np.abs(yf))
plt.title('Frekans Spektrumu')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.grid()
plt.show()