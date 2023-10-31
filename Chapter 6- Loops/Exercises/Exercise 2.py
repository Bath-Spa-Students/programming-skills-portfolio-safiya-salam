#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; 

#if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, 

#and then tell them the cost of their movie ticket.

# Prompt for asking the user's age
x = "How old are you? "

# Additional instruction for the user
y = "\nEnter 'quit' when you are finished. "

# Loop for continuous interaction with the user
while True:
    # Asking for the user's age
    age = input(x)

    # Checking if the user wants to quit the program
    if age == 'quit':
        break

    # Converting the input age to an integer
    age = int(age)

    # Evaluating the ticket price based on the user's age
    if age < 3:
        print("  You can get in for free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
