# Hash tables are dictionaries

# Create a hash table
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})

# Print the hash table
print(items1)

# Create an empty hash table
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3

# Print the new hash tale
print(items2)

# Print a specific item
print(items2["key2"])

# Replace an item
items2["key2"] = "two"

# Print the replaced item
print(items2["key2"])