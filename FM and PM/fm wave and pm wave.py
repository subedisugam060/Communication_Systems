import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
fs = 10000  # Sampling frequency
T = 1       # Duration in seconds
t = np.linspace(0, T, fs*T)  # Time vector

# Message signal (modulating signal)
fm = 5  # Message frequency in Hz
Am = 1  # Message amplitude
m_t = Am * np.cos(2 * np.pi * fm * t)  # Message signal

# Carrier signal
fc = 100  # Carrier frequency in Hz
Ac = 1    # Carrier amplitude
carrier = Ac * np.cos(2 * np.pi * fc * t)  # Carrier wave

# FM Modulation (higher kf for clearer effect)
kf = 200  # Frequency sensitivity
s_fm = Ac * np.cos(2 * np.pi * fc * t + kf * np.cumsum(m_t) / fs)

# PM Modulation (higher kp for clearer effect)
kp = 10  # Phase sensitivity
s_pm = Ac * np.cos(2 * np.pi * fc * t + kp * m_t)

# Zoom into first 0.1s for clarity
zoom_idx = int(0.1 * fs)

# Plot signals
plt.figure(figsize=(12, 8))

# Message signal
plt.subplot(4, 1, 1)
plt.plot(t[:zoom_idx], m_t[:zoom_idx], 'g', linestyle='dashed', linewidth=2)
plt.title(f"Message Signal (m(t)) | Frequency = {fm} Hz, Amplitude = {Am}")
plt.ylabel("Amplitude")
plt.grid()

# Carrier signal
plt.subplot(4, 1, 2)
plt.plot(t[:zoom_idx], carrier[:zoom_idx], 'k', linewidth=1)
plt.title(f"Carrier Signal | Frequency = {fc} Hz, Amplitude = {Ac}")
plt.ylabel("Amplitude")
plt.grid()

# FM Signal
plt.subplot(4, 1, 3)
plt.plot(t[:zoom_idx], s_fm[:zoom_idx], 'b', linewidth=1.5)
plt.title(f"Frequency Modulated Signal (FM) | kf = {kf}")
plt.ylabel("Amplitude")
plt.grid()

# PM Signal
plt.subplot(4, 1, 4)
plt.plot(t[:zoom_idx], s_pm[:zoom_idx], 'r', linewidth=1.5)
plt.title(f"Phase Modulated Signal (PM) | kp = {kp}")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
