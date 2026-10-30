import numpy as np
import matplotlib.pyplot as plt

# Define a simple discrete signal (impulse + random noise)
x = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) + np.random.normal(0, 0.5, 11)

# Define different filters
moving_avg_filter = np.array([1/3, 1/3, 1/3])  # Smoothing Filter
sharpening_filter = np.array([-1, 2, -1])      # Sharpening Filter
edge_detection_filter = np.array([-1, 0, 1])   # Edge Detection Filter (Derivative)

# Apply convolution with different filters
y_avg = np.convolve(x, moving_avg_filter, mode='same')
y_sharp = np.convolve(x, sharpening_filter, mode='same')
y_edge = np.convolve(x, edge_detection_filter, mode='same')

# Plot results
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(x, label="Original Signal", marker='o', linestyle='dashed')
plt.plot(y_avg, label="Smoothed (Moving Avg)", marker='s')
plt.legend()
plt.title("Moving Average Filter (Smoothing)")

plt.subplot(3, 1, 2)
plt.plot(x, label="Original Signal", marker='o', linestyle='dashed')
plt.plot(y_sharp, label="Sharpened Signal", marker='s')
plt.legend()
plt.title("Sharpening Filter")

plt.subplot(3, 1, 3)
plt.plot(x, label="Original Signal", marker='o', linestyle='dashed')
plt.plot(y_edge, label="Edge Detected Signal", marker='s')
plt.legend()
plt.title("Edge Detection Filter")

plt.tight_layout()
plt.show()
