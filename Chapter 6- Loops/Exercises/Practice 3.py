#Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100.

# Initialize a variable to store the sum
sum = 0

# Use a for loop to iterate through numbers from 1 to 100 (inclusive)
for num in range(1, 101):
    # Add the current number to the total sum
    sum += num

# Print the result
print("The sum of numbers from 1 to 100 is:", sum)
