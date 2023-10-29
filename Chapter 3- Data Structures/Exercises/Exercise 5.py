#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

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
