import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, wiener

# Generate a simple message signal (sine wave)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration
f_msg = 50  # Message frequency
x = np.sin(2 * np.pi * f_msg * t)  # Original signal

# Define a time-varying channel impulse response (simulating wireless effects)
h = np.exp(-t) * np.cos(2 * np.pi * 5 * t)  # Example of multipath fading

# Simulate received signal (convolution with channel + noise)
y = convolve(x, h, mode='same') + 0.1 * np.random.randn(len(t))  # Adding some noise

# Apply Wiener filter for equalization
x_estimated = wiener(y, mysize=29)  # Wiener filter to recover signal

# Plot the results
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x, label="Original Signal")
plt.title("Original Signal (Message)")
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, y, label="Received Signal (Distorted by Channel)", color='r')
plt.title("Received Signal with Channel Effects")
plt.legend()
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, x_estimated, label="Recovered Signal (After Equalization)", color='g')
plt.title("Recovered Signal After Channel Equalization")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
