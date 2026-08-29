import os                   #importing os and pandas module
import pandas as pd

df = pd.read_csv('student_performance.csv')         #loading CSV into dataframe

print("The first 5 rows are: \n")                   #printing first 5 rows
print(df.head())
print(f"Number of Rows and Columns: {df.shape}\n")      #printing no. of rows and columns

columnNameList=df.columns.tolist()
printList =", ".join(columnNameList)
print(f"Column Names: {printList}")                    #printing column names

hasMissingValues = df.isnull().values.any()
print("\nHas missing values? :")                           #checking whether dataset has missing values
print(hasMissingValues)

avgScore = df['Final_Score'].mean()                 #calculating average final score
print(f"\nAverage Final Score: {avgScore}")

maxScoreStud = df.loc[df['Final_Score'].idxmax(), 'Student']    #printing student with max score
print(f"\nStudent with the Highest Final Score:\n{maxScoreStud}")

df['Improvement'] = df['Final_Score'] - df['Previous_Score']        #creating improvement column
print("\nStudents with Attendance >= 80:")                          #displaying students with attendance>=80
print(df[df['Attendance'] >= 80]['Student'])

df_sorted = df.sort_values(by='Final_Score', ascending=False)       #sort data frame in descending order
os.makedirs('new', exist_ok=True)                               #making directory for the processed file

df_sorted.to_csv('new/processed_student_performance.csv', index=False)          #saving processed data frame
