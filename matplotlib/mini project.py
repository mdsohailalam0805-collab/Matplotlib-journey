
# students marks predictor

import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Student": ["sonu", "Harsh", "Sohail", "Waseem", "Altamash", "shivam"],
    "Math": [78, 65, 90, 72, 85, 60],
    "Python": [85, 70, 95, 80, 88, 65],
    "ML": [80, 68, 92, 75, 90, 62]
}

df = pd.DataFrame(data)

# Average Marks
df["Average"] = df[["Math", "Python", "ML"]].mean(axis=1)

print(df)

# 1. Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df["Student"], df["Python"])
plt.xlabel("Students")
plt.ylabel("Python Marks")
plt.title("Student-wise Python Marks")
plt.show()

# 2. Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df["Student"], df["Math"], marker="o", label="Math")
plt.plot(df["Student"], df["Python"], marker="o", label="Python")
plt.plot(df["Student"], df["ML"], marker="o", label="ML")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.legend()
plt.show()

# 3. Average Marks
plt.figure(figsize=(10, 5))
plt.bar(df["Student"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()

# 4. Pie Chart
subject_avg = [
    df["Math"].mean(),
    df["Python"].mean(),
    df["ML"].mean()
]

subjects = ["Math", "Python", "ML"]

plt.figure(figsize=(7, 7))
plt.pie(subject_avg, labels=subjects, autopct="%1.1f%%")
plt.title("Subject-wise Average Marks")
plt.show()

# 5. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Python"], bins=5)
plt.xlabel("Python Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Python Marks")
plt.show()