# Find the greatest common denominator of two numbers

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b

    return a

# Print results
print(gcd(60, 96))
print(gcd(10, 100))