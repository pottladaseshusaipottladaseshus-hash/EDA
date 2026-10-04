import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df[["Age", "Marks"]].describe())

print("\nAverage marks by department:")
print(df.groupby("Department")["Marks"].mean())

plt.figure(figsize=(7, 4))
df.groupby("Department")["Marks"].mean().plot(kind="bar")

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.savefig("average_marks.png")
plt.show()