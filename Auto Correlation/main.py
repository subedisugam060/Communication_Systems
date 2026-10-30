import numpy as np
import matplotlib.pyplot as plt

# Generate time vector
t = np.linspace(0, 1, 100, endpoint=False)

# Create a sine wave signal
x = np.sin(2 * np.pi * 5 * t)

# Compute auto-correlation
auto_correlation = np.correlate(x, x, mode='full')
lags = np.arange(-len(x) + 1, len(x))

# Plot original signal
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x, label="Original Signal")
plt.title("Original Signal (Sine Wave)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Plot auto-correlation
plt.subplot(2, 1, 2)
plt.plot(lags, auto_correlation)
plt.title("Auto-Correlation of the Signal")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid()

plt.tight_layout()
plt.show()
