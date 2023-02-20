# Ordered searching algorithm

# Create a list of items to search
to_search = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6, 91]

# Sort the items
to_search = sorted(to_search)

def binary_search(item, items):
    # Get size of list
    list_size = len(items) - 1

    # Start at the ends of the list
    lower_idx = 0
    upper_idx = list_size

    while lower_idx <= upper_idx:
        # Calculate midpoint
        midpoint = (lower_idx + upper_idx) // 2

        # Return index if item is found
        if items[midpoint] == item:
            return midpoint

        # Get next midpoint if item is not found
        if item > items[midpoint]:
            lower_idx = midpoint + 1
        else:
            upper_idx = midpoint - 1

    if lower_idx > upper_idx:
        return None
    

# Testing algorithm
print(binary_search(8, to_search))
print(binary_search(88, to_search))
