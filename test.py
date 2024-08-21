import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv("data.csv")

# Extract data from the dataframe
objects = df["Object"]
masses = df["Mass (kg)"]

# Define a range of velocities from 1 m/s to 0.999c
c = 3e8  # Speed of light in m/s
velocity_grid = np.logspace(1, np.log10(0.9999999 * c), num=10000)  # Velocity from 1 m/s to 0.999c

# Relativistic kinetic energy formula: KE = (gamma - 1) * m * c^2, where gamma = 1 / sqrt(1 - (v/c)^2)
def relativistic_ke(mass, velocity):
    gamma = 1 / np.sqrt(1 - (velocity/c)**2)
    return (gamma - 1) * mass * c**2

# Plot velocity vs. relativistic kinetic energy for each object
plt.figure(figsize=(10, 6))

for i, obj in enumerate(objects):
    mass = masses[i]
    # Calculate relativistic kinetic energy for the velocity grid
    kinetic_energy = relativistic_ke(mass, velocity_grid)
    # Plot the curve for this object
    plt.plot(velocity_grid, kinetic_energy, label=obj)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Relativistic Kinetic Energy (Joules)')
plt.title('Velocity vs. Relativistic Kinetic Energy for Various Objects (Logarithmic Scale)')
plt.grid(True, which="both", ls="--")
plt.legend()

# Display the plot
plt.show()
