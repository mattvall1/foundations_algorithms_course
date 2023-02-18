# Bubble sorting algorithm
def bubble_sort(dataset):
    for outer_loop in range(len(dataset) - 1, 0, -1):
        for inner_loop in range(outer_loop):
            if dataset[inner_loop] > dataset[inner_loop+1]:
                item = dataset[inner_loop]
                dataset[inner_loop] = dataset[inner_loop+1]
                dataset[inner_loop+1] = item
        # Print current state
        print("Iteration: ", dataset)

def main():
    # Create a list of items to sort
    to_sort = [23, 8, 15, 17, 4, 40, 11, 32, 83, 6]
    bubble_sort(to_sort)
    print("Result: ", to_sort)

if __name__ == "__main__":
    main()