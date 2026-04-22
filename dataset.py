import pandas as pd
import matplotlib.pyplot as plt
import re

# 👉 Enable multiple figures at same time
plt.ion()

# Load dataset
df = pd.read_csv('company_dataset.csv')

# Take only 20 records
df_20 = df.head(20).copy()

# ------------------ Data Cleaning ------------------

# Ratings to numeric
df_20['ratings'] = pd.to_numeric(df_20['ratings'], errors='coerce')

# Clean review count
def clean_reviews(x):
    x = str(x)
    x = re.sub(r'[^0-9.]', '', x)
    return float(x) if x else None

df_20['review_count'] = df_20['review_count'].apply(clean_reviews)

# Extract employee count
df_20['employee_count'] = df_20['employees'].str.extract(r'(\d+)').astype(float)

# ------------------ 1. Pie Chart ------------------
year_counts = df_20['years'].value_counts()

plt.figure()
plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%')
plt.title("Companies Year-wise Distribution")
plt.show()

# ------------------ 2. Funnel Chart ------------------
review_sorted = df_20.sort_values(by='review_count', ascending=False)

plt.figure()
plt.barh(review_sorted['name'], review_sorted['review_count'])
plt.title("Funnel Chart (Review-wise)")
plt.xlabel("Review Count")
plt.ylabel("Company")
plt.gca().invert_yaxis()
plt.show()

# ------------------ 3. Top 10 HQ ------------------
print("\nTop 10 Companies with Headquarters:\n")

top_10 = df_20[['name', 'hq']].head(10)

for index, row in top_10.iterrows():
    print(f"{row['name']}  -->  {row['hq']}")

# ------------------ 4. Bar Chart ------------------
plt.figure()
plt.bar(df_20['name'], df_20['ratings'])
plt.xticks(rotation=90)
plt.title("Company Ratings")
plt.xlabel("Company")
plt.ylabel("Rating")
plt.show()

# ------------------ 5. Line Chart ------------------
plt.figure()
plt.plot(df_20['name'], df_20['employee_count'], marker='o')
plt.xticks(rotation=90)
plt.title("Employee Count Trend")
plt.xlabel("Company")
plt.ylabel("Employee Count")
plt.show()

# Keep windows open
plt.ioff()
plt.show()