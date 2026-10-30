import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Sampling parameters
fs = 100000  # Sampling frequency (100 kHz)
t = np.linspace(0, 0.02, int(fs * 0.02))  # Time vector (20 ms)

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

# Simulating the effect of charging and discharging times
# We approximate the RC circuit behavior using a low-pass filter

def envelope_detector(signal, cutoff, fs, order=2):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)

# Different capacitor charge/discharge time constants
s_env_fast = envelope_detector(s_rect, fm * 3, fs)  # Fast charging (Good tracking)
s_env_slow = envelope_detector(s_rect, fm * 0.5, fs)  # Slow charging (Poor tracking)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, s, 'r')
plt.title("AM Modulated Signal")
plt.xlabel("Time [s]")

plt.subplot(3, 1, 2)
plt.plot(t, s_rect, 'k', alpha=0.5, label="Rectified Signal")
plt.plot(t, s_env_fast, 'g', label="Fast Envelope Detection (Good)")
plt.legend()
plt.title("Fast Charging - Good Envelope Tracking")
plt.xlabel("Time [s]")

plt.subplot(3, 1, 3)
plt.plot(t, s_rect, 'k', alpha=0.5, label="Rectified Signal")
plt.plot(t, s_env_slow, 'b', label="Slow Envelope Detection (Poor)")
plt.legend()
plt.title("Slow Charging - Poor Envelope Tracking")
plt.xlabel("Time [s]")

plt.tight_layout()
plt.show()
