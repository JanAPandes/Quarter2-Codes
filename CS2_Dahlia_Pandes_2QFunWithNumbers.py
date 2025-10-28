#Quarter 2 FA 3 - Sum of numbers to your age - Graded (From Study Guide 2 - Quarter 2)

'''

Goal: Demonstrate your understanding of Python iterative structures by creating a program that uses simple loops to sum up numbers according to a given input and display the computed output.

Role: You are a junior software developer designing a simple math utility.

Audience: your teachers and classmates.

Situation: You are working on a "Fun with Numbers" app. 

Product: A mini app that asks the user for their age and then calculates and displays the total sum of all numbers from 1 up to that age.

Standards: The mini app should run without errors and display the correct computed value.

Instructions and General Algorithm:

Open your Python IDE and create 2 variables, one for input and another for accumulating your sum.

Have an input for the age of your user.

Use a loop of your choice to count up from a starting number to the age of your user.
Add the present value of your counter to the sum variable.

Display your answer.

Upload your code to the instructed K-Hub activity using the following filename:
CS2_Section_Surname_2QFunWithNumbers.py

'''

age = int(input("Hi there! Please enter your age:"))
count = 0

for i in range(1,age+1):
    count += i
print(f"The sum of all numbers from 1 to {age} is: {count}")