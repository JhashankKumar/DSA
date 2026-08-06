# find least common multiple of two numbers

from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    result = lcm(n, m)
    print(f"The least common multiple of {n} and {m} is: {result}")

if __name__ == "__main__":
    main()

# inbuilt lcm function in Python 3.9 and above
from math import lcm as math_lcm
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
result = math_lcm(n, m)
print(f"The least common multiple of {n} and {m} using math.lcm is: {result}")