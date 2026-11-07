# Factorial of N
"""
Given a positive integer, n. Find the factorial of n.

Examples :
Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120

Input: n = 4
Output: 24
Explanation: 1 x 2 x 3 x 4 = 24

Constraints:
0 ≤ n ≤ 12
"""

"""
Approach:
1. We can solve the factorial problem using a recursive approach.
2. The base case is when n is 0 or 1, in which case the factorial is 1.
3. For n > 1, we can find the factorial by recursively calling the function with n-1 and multiplying the result by n.
4. The final result can be obtained by returning the result of the recursive call.
"""

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

if __name__ == "__main__":
    # Test cases
    print(factorial(5))  # Output: 120
    print(factorial(4))  # Output: 24
    print(factorial(0))  # Output: 1
    print(factorial(1))  # Output: 1
    print(factorial(12))  # Output: 479001600