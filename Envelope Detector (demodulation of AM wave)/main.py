import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Sampling parameters
fs = 100000  # Sampling frequency (100 kHz)
t = np.linspace(0, 0.02, int(fs * 0.02))  # Time vector (20 ms) - FIXED

# Message Signal (Low frequency)
fm = 1000  # Message frequency (1 kHz)
m = np.cos(2 * np.pi * fm * t)  # Message signal

# Carrier Signal (High frequency)
fc = 10000  # Carrier frequency (10 kHz)
carrier = np.cos(2 * np.pi * fc * t)  # Carrier signal

# AM Modulation (DSB with Carrier)
mu = 0.7  # Modulation index
s = (1 + mu * m) * carrier  # Modulated signal

# Envelope Detection (Rectification)
s_rect = np.abs(s)  # Full-wave rectification

# Low-Pass Filter (Butterworth)
def lowpass_filter(signal, cutoff, fs, order=2):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)

s_env = lowpass_filter(s_rect, fm * 1.5, fs)  # Filtering to extract the envelope

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, m, 'b')
plt.title("Message Signal (Original)")
plt.xlabel("Time [s]")

plt.subplot(3, 1, 2)
plt.plot(t, s, 'r')
plt.title("AM Modulated Signal")
plt.xlabel("Time [s]")

plt.subplot(3, 1, 3)
plt.plot(t, s_env, 'g')
plt.title("Demodulated Signal (Envelope Detector)")
plt.xlabel("Time [s]")

plt.tight_layout()
plt.show()
