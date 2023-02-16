# Power and Factorial examples

def power(num, to_power):
    if to_power == 0:
        return 1
    else:
        return num * power(num, to_power-1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Print results of examples
print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 35, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
