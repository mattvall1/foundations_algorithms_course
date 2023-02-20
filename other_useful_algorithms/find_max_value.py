# Max value algorithm

# Create a list of items
numbers = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6, 91]

def find_max(items):
    # Break condition if we are at the last item
    if(len(items)) == 1:
        return items[0]

    # Get first ite and call function again
    option_1 = items[0]
    option_2 = find_max(items[1:])

    # Perform the comparison when there is only two items left
    if option_1 > option_2:
        return option_1
    else:
        return option_2

# Test algorithm
print(find_max(numbers))
   