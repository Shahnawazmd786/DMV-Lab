import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

# Create pie chart
plt.pie(sizes, labels=labels)

# Title
plt.title("Simple Pie Chart")

# Show chart
plt.show()
