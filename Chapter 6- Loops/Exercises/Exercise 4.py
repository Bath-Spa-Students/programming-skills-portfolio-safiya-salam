#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
#Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, 
#such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, 
#print a message listing each sandwich that was made.

# List of sandwich orders
sandwich_orders = ['PBNJ', 'grilled cheese', 'chicken', 'beef']

# List to store finished sandwiches
finished_sandwiches = []

# Process the sandwich orders
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


