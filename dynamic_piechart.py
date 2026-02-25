import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Data
labels = ['A', 'B', 'C', 'D']

# Create figure
fig, ax = plt.subplots()

# Update function
def update(frame):
    ax.clear()  # clear previous pie chart

    # Generate new values dynamically
    sizes = [random.randint(10, 40) for _ in labels]

    # Draw pie chart
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')

    ax.set_title("Animated Pie Chart")

# Animation (updates every 1 second)
ani = FuncAnimation(fig, update, interval=1000)

plt.show()