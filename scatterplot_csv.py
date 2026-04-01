import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Md-Shahnawaz_DMV_lab\Clean_Students_Performance.csv")


sns.set(style="whitegrid")

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="packet_count",
    y="byte_volume_mb",
    hue="attack_type",
    palette="Set2",
    s=80
)

# Detect outliers using IQR
Q1 = df["byte_volume_mb"].quantile(0.25)
Q3 = df["byte_volume_mb"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["byte_volume_mb"] < Q1 - 1.5*IQR) | 
              (df["byte_volume_mb"] > Q3 + 1.5*IQR)]

# Highlight outliers
plt.scatter(
    outliers["packet_count"],
    outliers["byte_volume_mb"],
    color='red',
    edgecolor='black',
    s=120,
    label="Outliers"
)

plt.title("Scatter Plot: Packet Count vs Byte Volume")
plt.xlabel("Packet Count")
plt.ylabel("Byte Volume (MB)")
plt.legend()

plt.show()