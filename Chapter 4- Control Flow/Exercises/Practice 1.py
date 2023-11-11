#Write a python program with if statement that assigns 20 to the variable y and assigns 
#40 to the variable z if the variable & is greater than 100.

# Get user input for the variable &
variable = int(input("Enter the value for variable &: "))

# Check if the variable & is greater than 100
if variable >= 100:
    # Assign 20 to variable y
    y = 20
    # Assign 40 to variable z
    z = 40
    print("Variable & is greater than 100. Assigning 20 to y and 40 to z.")
else:
    print("Variable & is not greater than 100. No assignment to y and z.")

# Print the values of y and z
try:
    print("y =", y)
    print("z =", z)
except NameError:
    print("y and z are not defined because variable & is not greater than 100.")
