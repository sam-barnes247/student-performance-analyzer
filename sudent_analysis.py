import pandas as pd
import matplotlib.pyplot as plt
students = [
    {"name": "Khalifa", "age": 18, "score": 85},
    {"name": "Ama", "age": 19, "score": 72},
    {"name": "Kojo", "age": 18, "score": 64},
    {"name": "Esi", "age": 20, "score": 91},
    {"name": "Yaw", "age": 19, "score": 55}
]

print(students)

total_score = sum(student["score"] for student in students)
average_score = total_score / len(students)

print("Average score:", average_score)
highest_score = max(students, key=lambda student: student["score"])
lowest_score = min(students, key=lambda student: student["score"])

print("Highest score:", highest_score["name"], highest_score["score"])
print("Lowest score:", lowest_score["name"], lowest_score["score"])
for student in students:
    if student["score"] >= 80:
        grade = "A"
    elif student["score"] >= 70:
        grade = "B"
    elif student["score"] >= 60:
        grade = "C"
    elif student["score"] >= 50:
        grade = "D"
    else:
        grade = "F"

    print(student["name"], "Grade:", grade)
    passed_students = sum(1 for student in students if student["score"] >= 50)
pass_rate = (passed_students / len(students)) * 100

print("Pass rate:", pass_rate, "%")
df = pd.DataFrame(students)
print(df)
print(df.info())
print(df["score"].describe())
high_scorers = df[df["score"] >= 70]
print(high_scorers)
sorted_students = df.sort_values(by="score", ascending=False)
print(sorted_students)
df["performance"] = df["score"].apply(
    lambda score: "Excellent" if score >= 80
    else "Good" if score >= 70
    else "Average" if score >= 60
    else "Needs Improvement"
)

print(df)
plt.bar(df["name"], df["score"])

plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")

plt.show()
plt.bar(df["name"], df["score"])

plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
df.to_csv("student_data.csv", index=False)

print("Data saved successfully!")
print("\n--- KEY INSIGHTS ---")
print("Average score:", round(average_score, 2))
print("Top student:", highest_score["name"])
print("Lowest student:", lowest_score["name"])
print("Pass rate:", pass_rate, "%")