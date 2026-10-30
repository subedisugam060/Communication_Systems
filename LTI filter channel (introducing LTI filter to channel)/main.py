import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Generate a transmitted signal (high-frequency sine wave)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2 * np.pi * 100 * t)  # 100 Hz sine wave

# Define an LTI channel: Low-Pass Butterworth Filter
def lowpass_filter(signal, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, signal)

# Apply the LTI channel (low-pass filter with cutoff at 50 Hz)
cutoff_freq = 50
y = lowpass_filter(x, cutoff_freq, fs)

# Plot the original and filtered signals
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, x, label="Transmitted Signal (100 Hz)")
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, y, label="Received Signal (After LTI Filter)", color='r')
plt.title("Received Signal (Low-Pass Filtered)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
