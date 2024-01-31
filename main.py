import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Replace this with your actual data from the AMG8833 sensor
sensor_data = np.loadtxt('sensor_data.txt')

#sensor_data = np.random.rand(8, 8) * 100  # Replace with your actual data

# Create a grid for the heatmap
x, y = np.meshgrid(np.arange(8), np.arange(8))

# Create a finer grid for smoother visualization
xi, yi = np.meshgrid(np.linspace(0, 7, 100), np.linspace(0, 7, 100))

# Interpolate the data for smoother visualization
zi = griddata((x.flatten(), y.flatten()), sensor_data.flatten(), (xi, yi), method='cubic')

# Create the heatmap
plt.imshow(zi, extent=(0, 7, 0, 7), origin='lower', cmap='plasma')

# Add colorbar for reference
plt.colorbar()

# Save the plot as an image file
plt.savefig('heatmap.png')

# Don't call plt.show() to avoid the warning
