import numpy as np
import matplotlib.pyplot as plt

# Generate time vector
t = np.linspace(0, 1, 100, endpoint=False)

# Create two sinusoidal signals
x = np.sin(2 * np.pi * 5 * t)  # Signal 1 (sine wave)
y = np.sin(2 * np.pi * 5 * t + np.pi/4)  # Signal 2 (shifted sine wave)

# Compute cross-correlation
correlation = np.correlate(x, y, mode='full')
lags = np.arange(-len(x) + 1, len(x))

# Plot signals
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x, label="Signal 1 (Original)")
plt.plot(t, y, label="Signal 2 (Shifted)", linestyle="dashed")
plt.title("Two Signals")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Plot cross-correlation
plt.subplot(3, 1, 2)
plt.plot(lags, correlation)
plt.title("Cross-Correlation of Two Signals")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid()

plt.tight_layout()
plt.show()
