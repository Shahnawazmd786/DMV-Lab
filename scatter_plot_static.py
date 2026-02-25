import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create scatter plot
plt.scatter(x, y)

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Grid")

# Add grid
plt.grid(True)

# Display graph
plt.show()