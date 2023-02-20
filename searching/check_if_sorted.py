# Check if searching algorithm works

# Create a list of items to search
unsorted_list = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6, 91]
sorted_list = sorted(unsorted_list)

def is_sorted(items):
    # Use brute force
    for i in range(0, len(items) - 1):
        if items[i] > items[ i + 1]:
            return False
    
    # If we get here, the list must be sorted
    return True

def is_sorted_pythonic(items):
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))

# Testing algorithm
print(is_sorted(unsorted_list))
print(is_sorted(sorted_list))

print(is_sorted_pythonic(unsorted_list))
print(is_sorted_pythonic(sorted_list))
