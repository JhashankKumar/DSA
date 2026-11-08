# Fibonacci Number using Recursion
"""

The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
Constraints:
0 <= n <= 30
"""

"""
Approach: Use Recursion
1. If n is 0, return 0.
2. If n is 1, return 1.
3. Otherwise, return the sum of the Fibonacci numbers of (n-1) and (n-2) using recursion.
"""

def fibonacci(n: int) -> int:
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    n = 4
    print(f"Fibonacci number F({n}) is: {fibonacci(n)}")  # Output: 3

    m = 5
    print(f"Fibonacci number F({m}) is: {fibonacci(m)}")