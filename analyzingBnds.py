import pandas as pd

# Replace 'path_to_file' with the path to your CSV file
data = pd.read_csv('./ALevelCSVFinal.csv')

al10_data = data[data['YearGroup'] == 'AL10']
average_points_per_student = al10_data.groupby(
    ['Student ID', 'First Name', 'Last Name', 'Chinese Name'])['AveragePoints'].mean().reset_index()


# Assuming 'AveragePoints' column exists and contains numerical values
top_10_students = average_points_per_student.sort_values(
    by='AveragePoints', ascending=False).head(10)


print(top_10_students)
top_10_students.to_csv('./top_10_al10.csv', index=False)
