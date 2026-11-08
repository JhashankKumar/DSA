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


"""
Approach 2: Use Dynamic Programming
1. Create a 2D array dp of size m x n, initialized with 1s, since there is only one way to reach any cell in the first row or first column.
2. Iterate through the grid starting from cell (1, 1) to cell (m-1, n-1).
3. For each cell (i, j), update dp[i][j] as the sum of the unique paths from the cell above (i-1, j) and the cell to the left (i, j-1).
4. The final result will be stored in dp[m-1][n-1], which represents the number of unique paths to reach the bottom-right corner.
"""

def unique_paths_dp(m: int, n: int) -> int:
    # Create a 2D array dp of size m x n, initialized with 1s
    dp = [[1] * n for _ in range(m)]

    # Iterate through the grid starting from cell (1, 1)
    for i in range(1, m):
        for j in range(1, n):
            # Update dp[i][j] as the sum of unique paths from the cell above and the cell to the left
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # The final result is stored in dp[m-1][n-1]
    return dp[m - 1][n - 1]

# Example usage
if __name__ == "__main__":
    m = 3
    n = 7
    print(f"Number of unique paths in a {m}x{n} grid is: {unique_paths(m, n)}")  # Output: 28

    p = 3
    q = 2
    print(f"Number of unique paths in a {p}x{q} grid is: {unique_paths(p, q)}")  # Output: 3

    # Using dynamic programming approach
    print(f"Number of unique paths in a {m}x{n} grid (DP) is: {unique_paths_dp(m, n)}")  # Output: 28   