# House Robber Problem
"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into 
on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

"""
Approach: Dynamic Programming
We can use dynamic programming to solve this problem. Let dp[i] represent the maximum amount of money that can be robbed from the first i houses.
The recurrence relation is as follows:
- dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]) for i >= 2
- dp[0] = 0 (no houses to rob)
- dp[1] = nums[0] (only one house to rob)
"""

def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * (n + 1)
    dp[0] = 0  # Base case: no houses to rob
    dp[1] = nums[0]  # Base case: only one house to rob

    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

    return dp[n]

if __name__ == "__main__":
    # Test cases
    print(rob([1, 2, 3, 1]))  # Output: 4
    print(rob([2, 7, 9, 3, 1]))  # Output: 12
    print(rob([2, 1, 1, 2]))  # Output: 4