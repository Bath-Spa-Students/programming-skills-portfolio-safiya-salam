# Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know about each pet.
  
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'Cat',
    'name': 'John',
    'owner': 'Guido',
    'weight': 14,
    'eats': 'Fish',
}
pets.append(pet)

pet = {
    'animal type': 'Gold Fish',
    'name': 'Billy',
    'owner': 'Tiffany',
    'weight': 2,
    'eats': 'Fish Food',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Peso',
    'owner': 'Eric',
    'weight': 27,
    'eats': 'Bones',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
