# calculate greatest common divisor of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
result = gcd(n, m)
print(f"The greatest common divisor of {n} and {m} is: {result}")

# python inbuilt gcd function
from math import gcd as math_gcd
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
result = math_gcd(n, m)
print(f"The greatest common divisor of {n} and {m} using math.gcd is: {result}")