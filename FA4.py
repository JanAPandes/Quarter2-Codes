#Quarter 2 FA 4 Student Scores per Subject (Based on SG 2)
'''

Problem Description

Write a Python program that:

Ask the user to enter the number of students and the number of subjects per student.

Use a nested loop to input the scores.

Compute each student’s average, and display it.

Compute the overall class average after all students’ scores are entered.

'''
stu = int(input("Enter number of students: "))
sub = int(input("Enter number of subjects: "))
sum_of_score = 0
sum_of_avg = 0
for stu in range(1,stu+1):
    print("Student", stu)
    for sub in range(1,sub+1):
        score = float(input(f"Enter score {sub}: "))
        sum_of_score += score
    avg = sum_of_score/sub
    sum_of_score = 0
    sum_of_avg += avg
    print(f"Average of Student {stu}: {avg}")
class_avg = sum_of_avg/stu
print(f"Class Average = {class_avg}")