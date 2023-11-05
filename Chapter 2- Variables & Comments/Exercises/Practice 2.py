#Write a python program that takes courses marks as input and then calculates average of all the courses. 
#After calculating the average, calculate the percentage of a student using total marks. 
#Assume the total of all the courses marks is 500 or take the total marks from the user as input.

# Taking input for the number of courses
courses = int(input("Enter the number of courses: "))

# Taking input for total marks
total = int(input("Enter the total marks: "))

# Initializing the sum of marks variable
sum = 0

# Taking input for marks of each course
for i in range(courses):
    marks = int(input(f"Enter the marks for course {i+1}: "))
    sum += marks

# Calculating the average
average = sum / courses

# Calculating the percentage
percentage = (sum / total) * 100

# Printing the average and percentage
print(f"The average marks is: {average}")
print(f"The percentage is: {percentage}%")
