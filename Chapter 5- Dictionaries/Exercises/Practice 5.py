#Write a Python program to merge two dictionaries into one.

# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dictionaries using dictionary unpacking
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)
