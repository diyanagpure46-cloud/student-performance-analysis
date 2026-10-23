
import pandas as pd
import numpy as np

# Load student dataset
df = pd.read_csv("student_data.csv")

# Subject columns
subjects = ["Maths", "Science", "English"]

# Calculate total and average marks
df["Total_Marks"] = df[subjects].sum(axis=1)
df["Average_Marks"] = np.round(
    df[subjects].mean(axis=1), 2
)

# Function to classify student performance
def classify_performance(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Needs Improvement"
    else:
        return "At Risk"

# Apply performance classification
df["Performance"] = df["Average_Marks"].apply(
    classify_performance
)

# Display overall summary
print("\nSTUDENT PERFORMANCE ANALYSIS")
print("=" * 35)
print("Total Students:", len(df))
print(
    "Overall Average Marks:",
    round(df["Average_Marks"].mean(), 2)
)
print(
    "Average Attendance:",
    round(df["Attendance"].mean(), 2), "%"
)

# Display subject-wise average marks
print("\nSUBJECT-WISE AVERAGES")
print(df[subjects].mean().round(2))

# Display top five students
print("\nTOP FIVE STUDENTS")
top_students = df.nlargest(5, "Average_Marks")
print(
    top_students[
        ["Name", "Average_Marks", "Performance"]
    ].to_string(index=False)
)

# Display performance category counts
print("\nPERFORMANCE SUMMARY")
print(df["Performance"].value_counts())

# Analyze attendance and average marks
correlation = np.corrcoef(
    df["Attendance"], df["Average_Marks"]
)[0, 1]

print("\nATTENDANCE ANALYSIS")
print(
    "Correlation between attendance and marks:",
    round(correlation, 2)
)

# Save complete analysis to a CSV file
df.to_csv("student_analysis_results.csv", index=False)

print("\nResults saved to student_analysis_results.csv")
print("Analysis completed successfully!")
