import matplotlib.pyplot as plt     #importing matplotlib and pandas module
import pandas as pd

df=pd.read_csv("data/processed_student_performance.csv")
#bar chart
plt.figure(figsize=(80, 5))

plt.bar(df['Student'], df['Final_Score'], color='orange', edgecolor='black')

plt.title('Student names vs final scores', fontsize=16)
plt.xlabel('Student Name (x-axis)', fontsize=12)
plt.ylabel('Final Score (y-axis)', fontsize=12)
plt.tight_layout()
plt.savefig("plots/final_scores.png")

#scatter graph
plt.figure(figsize=(8, 5))

plt.scatter(df['Hours_Studied'], df['Final_Score'],color='red', edgecolor='black', s=80)

plt.title('Hours studied vs final score', fontsize=16)
plt.xlabel('Hours Studied (x-axis)', fontsize=12)
plt.ylabel('Final Score (y-axis)', fontsize=12)

plt.tight_layout()
plt.savefig('plots/study_vs_scores.png')

#histogram

plt.figure(figsize=(8, 5))
plt.hist(df['Final_Score'],color='magenta', edgecolor='black')

plt.title('Distribution of Final Scores', fontsize=16)
plt.xlabel('Final Score Range (x-axis)', fontsize=12)
plt.ylabel('Number of Students (y-axis)', fontsize=12)

plt.tight_layout()

plt.savefig('plots/score_distribution.png')
plt.figure(figsize=(8, 5))

plt.scatter(df['Hours_Studied'], df['Improvement'],color='indigo', edgecolor='black', s=80)

plt.title('Study Hours vs Improvements', fontsize=16)
plt.xlabel('Hours Studied (x-axis)', fontsize=12)
plt.ylabel('Improvement (y-axis)', fontsize=12)

plt.tight_layout()
plt.savefig('plots/custom_plot.png')



