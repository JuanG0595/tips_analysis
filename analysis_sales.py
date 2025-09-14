import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")

print("Datafreame's first 5 rows")

print(df.head())

print("\n'Dataframe's statistical resume ")
print(df.describe())

print("Average tip:")
print(df["tip"].mean())

print("Max total bill")
print(df["total_bill"].max())
