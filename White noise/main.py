import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# Generate white noise
np.random.seed(42)  # For reproducibility
N = 1000  # Number of samples
white_noise = np.random.normal(0, 1, N)  # Mean=0, Variance=1

# Compute autocorrelation (normalized)
acf = correlate(white_noise, white_noise, mode='full') / N
lags = np.arange(-N+1, N)  # Corresponding lags

# Normalize to match delta function properties
acf = acf / np.max(acf)

# Theoretical Dirac Delta function (ideal case)
delta_function = np.zeros_like(acf)
delta_function[len(delta_function) // 2] = 1  # Dirac delta at lag=0

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(lags, acf, label="Empirical ACF (White Noise)", linestyle='-', color='b')
plt.stem(lags, delta_function, linefmt='r-', markerfmt='ro', basefmt='r', label="Theoretical Dirac Delta")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation Function of White Noise")
plt.legend()
plt.grid()
plt.show()
