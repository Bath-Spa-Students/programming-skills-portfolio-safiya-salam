#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Specify the condition to break the loop
condition = 6

# Use a for loop to iterate through the list of numbers
for num in numbers:
    # Check if the current number matches the specified condition
    if num == condition:
        print(f"Condition {condition} met. Exiting the loop.")
        break
    else:
        # Print the current number if the condition is not met
        print(num)

# This line will be executed after the loop is exited
print("Loop finished.")
