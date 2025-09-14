import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")

print("Datafreame's first 5 rows")

print(df.head())

print("\n'Dataframe's statistical resume")
print(df.describe())

print("Average tip:")
print(df["tip"].mean())

print("Max total bill")
print(df["total_bill"].max())

average_tip_size = df.groupby("size")["tip"].mean()

print("Average tip by size group:")
print(average_tip_size)

popular_day = df["day"].value_counts()
print("\nMost popular days of the week:")
print(popular_day)

print("Average tip plot")
plt.figure(figsize=(8,6))
plt.bar(x = average_tip_size.index, height = average_tip_size.values)
plt.title("Average tip by size group")
plt.xlabel("Group height")
plt.ylabel("Average tip (USD)")
plt.show()

plt.figure(figsize=(8,6))
plt.bar(x = popular_day.index, height = popular_day.values)
plt.title("Most popular days of the week")
plt.xlabel("Day of the week")
plt.ylabel("Clients amount")
plt.show()
