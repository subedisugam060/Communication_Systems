import numpy as np
import matplotlib.pyplot as plt

# Define a simple discrete signal (impulse + random noise)
x = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) + np.random.normal(0, 0.5, 11)

# Define a simple filter (Moving Average of 3 points)
h = np.array([1/3, 1/3, 1/3])  # Averages 3 neighboring values

# Perform discrete convolution using NumPy
y = np.convolve(x, h, mode='same')

# Plot the original and convolved signals
plt.figure(figsize=(8, 4))
plt.plot(x, label="Original Signal", marker='o', linestyle='dashed')
plt.plot(y, label="Convolved Signal (Smoothed)", marker='s')
plt.legend()
plt.title("Signal Convolution (Moving Average Filter)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


# The original signal:
# 𝑥[n]
# This represents the input signal, which consists of discrete values (a simple waveform with added noise).

# The filter (impulse response)
# ℎ[𝑛]:
# This represents a 3-point moving average filter, defined as:
# ℎ[𝑛]  = [1/3, 1/3, 1/3]
# It acts as a smoothing filter, averaging each sample with its two neighbors.

# The signal
# 𝑥[𝑛]
# x[n] is "smeared" by the filter ℎ[𝑛], creating a smoothed version of the input.
