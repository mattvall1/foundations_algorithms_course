# Quick sorting algorithm - pivot point selection

# Create a list of items to sort
to_sort = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6, 91]

def quick_sort(dataset, first, last):
    if first < last:
        # Calculate split point
        pivot_idx = partition(dataset, first, last)

        # Now sort split data - recursively
        quick_sort(dataset, first, pivot_idx - 1)
        quick_sort(dataset, pivot_idx + 1, last)

def partition(values, first, last):
    # Choose first item as pivot value
    pivot_value = values[first]

    # Set upper and lower indexes
    lower = first + 1
    upper = last

    # Search for crossing point
    complete = False
    while not complete:
        # Advance lower index
        while lower <= upper and values[lower] <= pivot_value:
            lower += 1

        # Advance upper index
        while upper >= lower and values[upper] >= pivot_value:
            upper -= 1

        # If both indexes cross, we've found the split point
        if upper < lower:
            complete = True
        else:
            temp_value = values[lower]
            values[lower] = values[upper]
            values[upper] = temp_value

    # When split point is found, exchange pivot value
    temp_values = values[first]
    values[first] = values[upper]
    values[upper] = temp_values

    # Return split point index
    return upper

print("Unsorted: ", to_sort)
quick_sort(to_sort, 0, len(to_sort) - 1)
print("Sorted: ", to_sort)