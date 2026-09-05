import matplotlib.pyplot as plt
import numpy as np


# ============================================
# NumPy + Matplotlib Sine Wave
# ============================================

# Create 50 evenly spaced values from 0 to 10
x = np.linspace(0, 10, 50)

# Calculate the sine of each X value
y = np.sin(x)


# ============================================
# Create the Sine Wave
# ============================================

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    y,
    linestyle="-.",
    color="green",
    linewidth=5
)


# ============================================
# Customize the Chart
# ============================================

plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Sin(X)")

# Add a semi-transparent dashed grid
plt.grid(
    True,
    color="red",
    linestyle="--",
    alpha=0.5
)


# Set the visible range of the axes
plt.xlim(2, 8)
plt.ylim(-0.5, 1)


# Improve the layout
plt.tight_layout()


# Display the chart
plt.show()