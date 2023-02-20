# Use a hashtable to count unique items

# Create some items with duplicates
fruits = ["apple", "banana", "orange", "cherry", "date", "mango", "elderberry", "fig", "cherry", "grapefruit", "honeydew", "cherry", "kiwi", "lemon", "apple", "mango", "nectarine", "kiwi", "orange", "pear", "quince", "banana", "banana"]

# Create a hashtable to perform the count
counter = dict()
for fruit in fruits:
    if fruit in counter.keys():
        counter[fruit] += 1
    else:
        counter[fruit] = 1

# Print counter
print(counter)
