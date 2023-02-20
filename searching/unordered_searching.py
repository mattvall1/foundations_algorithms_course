# Unordered searching algorithm

# Create a list of items to search
to_search = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6, 91]

def find_item(item, items):
    for i in range(0, len(items)):
        if item == items[i]:
            return i

    return None

# Testing algorithm
print(find_item(4, to_search))
print(find_item(44, to_search))
