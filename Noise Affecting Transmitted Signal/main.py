import numpy as np
import matplotlib.pyplot as plt

# Generate a simple digital signal (square wave)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector (1 second)
signal = np.sign(np.sin(2 * np.pi * 5 * t))  # Square wave signal

# Additive White Gaussian Noise (AWGN)
noise_power = 0.2  # Noise intensity
noise = np.sqrt(noise_power) * np.random.randn(len(t))  # Generate Gaussian noise
received_signal = signal + noise  # Add noise to the signal

# Plot original and noisy signals
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, signal, 'b', label="Original Signal")
plt.title("Original Digital Signal (Square Wave)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, received_signal, 'r', label="Noisy Signal")
plt.title("Noisy Signal (AWGN Channel)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
