#Write an if-else statement that assigns O to the variable b if the variable a is less than 10.
#Otherwise, it should assign 99 to the variable b.

# Get user input for the variable a
a = int(input("Enter the value for variable a: "))

# Check if the variable a is less than 10
if a < 10:
    # Assign 0 to variable b
    b = 0
    print("Variable a is less than 10. Assigning 0 to b.")
else:
    # Assign 99 to variable b
    b = 99
    print("Variable a is greater than 10. Assigning 99 to b.")

# Print the value of b
print("b =", b)
