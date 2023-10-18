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