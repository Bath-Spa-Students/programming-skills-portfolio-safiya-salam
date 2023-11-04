#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited. 
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

names = ['Tom', 'Mike', 'Joy']
for name in names:
    print(f'{name}! Want to come to my dinner party?')
# Jack can't make it! Let's invite Gary instead.
name = names[1].title()
print("\nSorry, " + name + " can't make it to dinner.")
del(names[1])
names.insert(1, 'Gary')

# Print the invitations again.
name = names[0].title()
print("\n" + name + ", Want to come to my dinner party?")

name = names[1].title()
print(name + ", Want to come to my dinner party?")

name = names[2].title()
print(name + ", Want to come to my dinner party?")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = names.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = names[0].title()
print(name + ", please come to dinner.")

name = names[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(names[0])
del(names[0])

# Prove the list is empty.
print(names)
