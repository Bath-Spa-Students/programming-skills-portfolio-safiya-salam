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