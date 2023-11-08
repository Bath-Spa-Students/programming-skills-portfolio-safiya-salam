#Given a Python list, write a program to remove all occurrences of item 20. Given list:
#list1 = [5, 20, 15, 20, 25, 50, 20] 

# List given 
list1 = [5, 20, 15, 20, 25, 50, 20]

# Removing all occurrences of item 20 using list comprehension
list1 = [item for item in list1 if item != 20]

# Printing the updated list
print("Modified list:", list1)
