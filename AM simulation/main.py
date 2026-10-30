import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fs = 5000  # Sampling frequency (Hz)
t = np.linspace(0, 0.02, fs)  # Time vector (0 to 20ms)
fm = 50   # Message signal frequency (Hz)
fc = 500  # Carrier frequency (Hz)
Ac = 1    # Carrier amplitude
Am = 0.5  # Message amplitude
mod_index = 1  # Modulation index (m = Am/Ac)

# Generate signals
message_signal = Am * np.cos(2 * np.pi * fm * t)  # Message signal
carrier_signal = Ac * np.cos(2 * np.pi * fc * t)  # Carrier signal
modulated_signal = (Ac + message_signal) * np.cos(2 * np.pi * fc * t)  # AM signal

# Plot the signals
plt.figure(figsize=(12, 6))

# Message signal
plt.subplot(3, 1, 1)
plt.plot(t, message_signal, 'g')
plt.title("Message Signal (Modulating Signal)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Carrier signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal, 'b')
plt.title("Carrier Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# AM signal
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, 'r')
plt.title("Amplitude Modulated (AM) Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
