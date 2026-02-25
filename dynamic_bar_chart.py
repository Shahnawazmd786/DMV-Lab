import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# Categories
categories = ['A', 'B', 'C', 'D', 'E']

# Create figure
fig, ax = plt.subplots()

# Initial values
values = [random.randint(5, 20) for _ in categories]

# Draw initial bars
bars = ax.bar(categories, values)

ax.set_ylim(0, 30)
ax.set_title("Dynamic Bar Chart")

# Function to update chart
def update(frame):
    new_values = [random.randint(5, 25) for _ in categories]

    for bar, val in zip(bars, new_values):
        bar.set_height(val)

# Animation (updates every 1 second)
ani = FuncAnimation(fig, update, interval=1000)

plt.show()