import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analyzer")
st.write("An interactive dashboard for analyzing student performance.")

students = [
    {"name": "Khalifa", "age": 18, "score": 85},
    {"name": "Ama", "age": 19, "score": 72},
    {"name": "Kojo", "age": 18, "score": 64},
    {"name": "Esi", "age": 20, "score": 91},
    {"name": "Yaw", "age": 19, "score": 55}
]

df = pd.DataFrame(students)
df["grade"] = df["score"].apply(
    lambda score: "A" if score >= 80
    else "B" if score >= 70
    else "C" if score >= 60
    else "D" if score >= 50
    else "F"
)

st.sidebar.header("🔎 Filter Students")

minimum_score = st.sidebar.slider(
    "Minimum Score",
    min_value=0,
    max_value=100,
    value=0
)

filtered_df = df[df["score"] >= minimum_score]

st.subheader("📋 Student Data")
st.dataframe(filtered_df, use_container_width=True)

average_score = filtered_df["score"].mean()
highest_score = filtered_df["score"].max()
lowest_score = filtered_df["score"].min()

col1, col2, col3 = st.columns(3)

col1.metric("Average Score", round(average_score, 2))
col2.metric("Highest Score", highest_score)
col3.metric("Lowest Score", lowest_score)

st.subheader("📈 Student Scores")

fig, ax = plt.subplots()

ax.bar(filtered_df["name"], filtered_df["score"])
ax.set_xlabel("Students")
ax.set_ylabel("Score")
ax.set_title("Student Scores")

st.pyplot(fig)