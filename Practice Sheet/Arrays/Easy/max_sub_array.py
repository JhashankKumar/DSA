# max subarray sum
"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.
"""

"""
Approach 1: Brute Force - O(n^2) Time and O(1) Space
The idea is to use two nested loops to find the sum of all possible subarrays and keep track of the maximum sum found so far. 
1. Initialize a variable max_sum to store the maximum sum found so far. Set it to a very small value (e.g., negative infinity).
2. Use two nested loops to iterate through all possible subarrays of the input array. The outer loop will fix the starting index of the subarray, and the inner loop will fix the ending index of the subarray.
3. For each subarray, calculate its sum and update max_sum if the current subarray sum is greater than max_sum.
4. After checking all possible subarrays, return max_sum as the result.
"""

def max_subarray_sum_brute_force(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    n = len(nums)
    
    # Iterate through all possible subarrays
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]  # Calculate the sum of the current subarray
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed
            
    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum (Brute Force):", max_subarray_sum_brute_force(arr))  # Output: 6

