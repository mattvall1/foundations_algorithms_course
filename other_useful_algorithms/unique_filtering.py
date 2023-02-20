# Use a hashtable to filter duplicate items

# Create some items with duplicates
fruits = ["apple", "banana", "orange", "cherry", "date", "mango", "elderberry", "fig", "cherry", "grapefruit", "honeydew", "cherry", "kiwi", "lemon", "apple", "mango", "nectarine", "kiwi", "orange", "pear", "quince", "banana", "banana"]

# Create a hashtable to perform the filter
filter_hashes = dict()
for fruit in fruits:
    filter_hashes[fruit] = 0

# Create a set from resulting keys
fruits_set = set(filter_hashes.keys())
print(fruits_set)
