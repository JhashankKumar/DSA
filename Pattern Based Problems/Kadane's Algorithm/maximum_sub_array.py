# Maximum Subarray Problem using Kadane's Algorithm

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
 

Follow up: If you have figured out the O(n) solution, try coding another solution 
using the divide and conquer approach, which is more subtle.
"""

"""
Approach: Kadane's Algorithm
1. Initialize two variables, max_so_far and max_ending_here, to the first element of the array.
2. Iterate through the array starting from the second element.
3. For each element, update max_ending_here to be the maximum of the current element and the sum of max_ending_here and the current element.
4. Update max_so_far to be the maximum of max_so_far and max_ending_here.
5. Return max_so_far as the result, which represents the largest sum of the contiguous subarray.
"""

def max_sub_array(nums):
    # Initialize max_so_far and max_ending_here to the first element of the array
    max_so_far = nums[0]
    max_ending_here = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update max_ending_here to be the maximum of the current element and the sum of max_ending_here and the current element
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        # Update max_so_far to be the maximum of max_so_far and max_ending_here
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage:
if __name__ == "__main__":
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(nums1))  # Output: 6

    nums2 = [1]
    print(max_sub_array(nums2))  # Output: 1

    nums3 = [5, 4, -1, 7, 8]
    print(max_sub_array(nums3))  # Output: 23