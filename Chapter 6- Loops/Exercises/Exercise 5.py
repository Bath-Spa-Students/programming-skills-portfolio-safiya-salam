#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
#and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
#Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami', 'PBNJ', 'grilled cheese', 'pastrami', 'chicken', 'beef', 'pastrami']
finished_sandwiches = []

print("we're sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I'm working on your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("\n")
for s in finished_sandwiches:
    print("I made your " + s + " sandwich.")
