import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector (1 second)
f_c = 100  # Carrier frequency (Hz)
f_d = 5  # Doppler shift (Hz)

# Generate a transmitted signal (sinusoidal wave)
x = np.sin(2 * np.pi * f_c * t)

# Define a time-variant impulse response with Doppler shift
h_t = np.exp(1j * 2 * np.pi * f_d * t)  # Complex exponential simulating Doppler effect

# Pass the signal through the LTV channel (multiplication in time domain)
y = np.real(x * h_t)  # Received signal (taking real part)

# Plot the transmitted and received signals
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, x, label="Transmitted Signal")
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, y, label="Received Signal (LTV Channel with Doppler Shift)", color='r')
plt.title("Received Signal (Time-Variant Effects)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
