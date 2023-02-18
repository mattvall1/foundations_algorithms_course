# Merge sorting algorithm

# Create a list of items to sort
to_sort = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6, 91]

def merge_sort(dataset):
    if len(dataset) > 1:
        # Find the midpoint and split into two arrays
        midpoint = len(dataset) // 2 
        left_array = dataset[:midpoint]
        right_array = dataset[midpoint:]

        # Recersively break the array 
        merge_sort(left_array)
        merge_sort(right_array)

        # Setup indexes
        lidx = 0 # Index into left array
        ridx = 0 # Index into right array
        midx = 0 # Index into merged array

        # Perform the merge
        while lidx < len(left_array) and ridx < len(right_array):
            if left_array[lidx] < right_array[ridx]:
                dataset[midx] = left_array[lidx]
                lidx += 1
            else:
                dataset[midx] = right_array[ridx]
                ridx += 1
            midx += 1

        # If left array has values, add them 
        while lidx < len(left_array):
            dataset[midx] = left_array[lidx]
            lidx += 1
            midx += 1

        # If right array has values, add them
        while ridx < len(right_array):
            dataset[midx] = right_array[ridx]
            ridx += 1
            midx += 1

# Test the merge sort with data
print("Unsorted: ", to_sort)
merge_sort(to_sort)
print("Sorted: ", to_sort)