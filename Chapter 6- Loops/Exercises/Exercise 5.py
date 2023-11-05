#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami,  
#and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
#Make sure no pastrami sandwiches end up in finished_sandwiches.

# List of sandwich orders
sandwich_orders = ['pastrami', 'PBNJ', 'grilled cheese', 'pastrami', 'chicken', 'beef', 'pastrami']

# List to store finished sandwiches
finished_sandwiches = []

# Notify the unavailability of pastrami
print("we're sorry, we're all out of pastrami today.")

# Remove all instances of pastrami from the sandwich orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Print a new line for separation
print("\n")

# Process the remaining sandwich orders
while sandwich_orders:
    # Pop the last sandwich order
    sandwich = sandwich_orders.pop()
    # Notify the working status
    print("I'm working on your " + sandwich + " sandwich.")
    # Add finished sandwich to the list
    finished_sandwiches.append(sandwich)

# Print a new line for separation
print("\n")

# Display the finished sandwiches
for s in finished_sandwiches:
    print("I made your " + s + " sandwich.")

