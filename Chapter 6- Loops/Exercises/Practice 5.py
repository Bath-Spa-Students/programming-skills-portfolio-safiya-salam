#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.

# Initialize a variable to store the largest number
largest_number = float('8')
# Use a while loop to repeatedly get user input
while True:
    # Get user input
    user_input = input("Enter a number (enter '0' to exit): ")

    # Check if the user wants to exit the loop
    if user_input == '0':
        break

    # Convert the user input to a float
    number = float(user_input)

    # Update the largest_number if the current number is greater
    if number > largest_number:
        largest_number = number

# Print the result
if largest_number == float('8'):
    print("No valid numbers were entered.")
else:
    print("The largest number entered is:", largest_number)
