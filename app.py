import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analyzer")
st.write("Upload a student CSV file and automatically analyze performance.")

# Default student data
students = [
    {"name": "Khalifa", "age": 18, "score": 85},
    {"name": "Ama", "age": 19, "score": 72},
    {"name": "Kojo", "age": 18, "score": 64},
    {"name": "Esi", "age": 20, "score": 91},
    {"name": "Yaw", "age": 19, "score": 55}
]

default_df = pd.DataFrame(students)

# CSV upload
uploaded_file = st.file_uploader(
    "📂 Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV uploaded successfully! 🎉")
else:
    df = default_df
    st.info("No CSV uploaded. Using the sample student data.")

# Check required columns
required_columns = {"name", "age", "score"}

if not required_columns.issubset(df.columns):
    st.error("Your CSV must contain these columns: name, age, score")
    st.stop()

# Grade calculation
df["grade"] = df["score"].apply(
    lambda score: "A" if score >= 80
    else "B" if score >= 70
    else "C" if score >= 60
    else "D" if score >= 50
    else "F"
)

# Sidebar filter
st.sidebar.header("🔎 Filter Students")

minimum_score = st.sidebar.slider(
    "Minimum Score",
    min_value=0,
    max_value=100,
    value=0
)

filtered_df = df[df["score"] >= minimum_score]

# Student table
st.subheader("📋 Student Data")
st.dataframe(filtered_df, use_container_width=True)

# Stop if filter produces no students
if filtered_df.empty:
    st.warning("No students match the selected score.")
    st.stop()

# Statistics
average_score = filtered_df["score"].mean()
highest_score = filtered_df["score"].max()
lowest_score = filtered_df["score"].min()
pass_rate = (filtered_df["score"] >= 50).mean() * 100

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Score", round(average_score, 2))
col2.metric("Highest Score", highest_score)
col3.metric("Lowest Score", lowest_score)
col4.metric("Pass Rate", f"{pass_rate:.1f}%")

# Chart
st.subheader("📈 Student Scores")

fig, ax = plt.subplots()

ax.bar(filtered_df["name"], filtered_df["score"])
ax.set_xlabel("Students")
ax.set_ylabel("Score")
ax.set_title("Student Scores")

st.pyplot(fig)

# Grade distribution
st.subheader("🎓 Grade Distribution")

grade_counts = filtered_df["grade"].value_counts().sort_index()

st.bar_chart(grade_counts)

# Automatic insights
st.subheader("🧠 Automatic Insights")

top_student = filtered_df.loc[
    filtered_df["score"].idxmax(), "name"
]

lowest_student = filtered_df.loc[
    filtered_df["score"].idxmin(), "name"
]

st.write(f"🏆 **Top student:** {top_student}")
st.write(f"📉 **Lowest-scoring student:** {lowest_student}")
st.write(f"👥 **Students analyzed:** {len(filtered_df)}")
st.write(f"✅ **Pass rate:** {pass_rate:.1f}%")