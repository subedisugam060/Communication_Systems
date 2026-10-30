import numpy as np
import matplotlib.pyplot as plt

# Generate a message signal
t = np.linspace(0, 1, 1000)  # Time vector
message_signal = 5 * np.sin(2 * np.pi * 5 * t)  # Original signal with amplitude 5

# Normalize the message signal
normalized_message = message_signal / np.max(np.abs(message_signal))

# Plot original and normalized signals
plt.figure(figsize=(8, 5))
plt.plot(t, message_signal, label="Original Message Signal", linestyle="dashed")
plt.plot(t, normalized_message, label="Normalized Message Signal", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Normalized Message Signal")
plt.legend()
plt.grid()
plt.show()
