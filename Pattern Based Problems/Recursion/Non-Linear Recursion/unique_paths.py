# Unique Paths Problem
"""
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:
1 <= m, n <= 100
"""

"""
Approach: Use Recursion
1. If m is 1 or n is 1, return 1 (base case).
2. Otherwise, return the sum of the unique paths from the cell above (m-1, n) and the cell to the left (m, n-1) using recursion.
"""

def unique_paths(m: int, n: int) -> int:
    # Base case: If either m or n is 1, there is only one unique path
    if m == 1 or n == 1:
        return 1
    else:
        # Recursive case: Sum of unique paths from the cell above and the cell to the left
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)


# Example usage
if __name__ == "__main__":
    m = 3
    n = 7
    print(f"Number of unique paths in a {m}x{n} grid is: {unique_paths(m, n)}")  # Output: 28

    p = 3
    q = 2
    print(f"Number of unique paths in a {p}x{q} grid is: {unique_paths(p, q)}")  # Output: 3