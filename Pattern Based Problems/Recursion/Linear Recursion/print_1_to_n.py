# Print 1 to N using Recursion
"""
Given an positive integer n, print numbers from 1 to n without using loops.

Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

Examples
Input: n = 5
Output: 1 2 3 4 5
Explanation: We have to print numbers from 1 to 5.

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Explanation: We have to print numbers from 1 to 10.

Constraints:
1 ≤ n ≤ 1000
"""

"""
Approach:
1. We can solve this problem using a recursive approach.
2. The base case is when n is 1, in which case we print 1
3. For n > 1, we can recursively call the function with n-1 and then print n after the recursive call.
4. This way, we will print numbers from 1 to n in increasing order.
"""

def printTillN(n: int) -> None:
    if n == 1:
        print(1, end=' ')  # Base case: print 1
    else:
        printTillN(n - 1)  # Recursive case: print numbers from 1 to n-1
        print(n, end=' ')  # Print n after the recursive call

if __name__ == "__main__":
    # Test cases
    printTillN(5)  # Output: 1 2 3 4 5
    print()  # New line for better readability
    printTillN(10)  # Output: 1 2 3 4 5 6 7 8 9 10