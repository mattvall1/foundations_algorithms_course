import time
# Simple countdown function using recursion

def countdown(x):
    if x == 0:
        print("Done")
        return
    else:
        x = x - 1
        print("Remaining:", x)
        time.sleep(0.25)
        # Re-run the function
        countdown(x)

countdown(10)