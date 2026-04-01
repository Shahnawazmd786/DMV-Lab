import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\lab\Downloads\archive (1)\StudentPerformanceFactors.csv")


df = df.iloc[:30, :30]


numeric_df = df.select_dtypes(include=['number'])


plt.figure()
numeric_df.boxplot()
plt.xticks(rotation=90)
plt.title("Boxplot of Dataset")
plt.show()