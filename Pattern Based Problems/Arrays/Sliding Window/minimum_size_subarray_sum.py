# Minimum Size Subarray Sum
"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

"""
Approach: Sliding Window Technique
1. Initialize two pointers, left and right, to represent the current window in the array.
2. Initialize a variable, current_sum, to keep track of the sum of the elements in the current window.
3. Initialize a variable, min_length, to store the minimum length of the subarray that meets the target sum.
4. Iterate through the array using the right pointer to expand the window and add the current element to current_sum.
5. While current_sum is greater than or equal to the target sum, update min_length with the current window size (right - left + 1) 
and move the left pointer to shrink the window, subtracting the element at the left pointer from current_sum.
6. Continue this process until the right pointer reaches the end of the array.
7. If min_length is still infinity, it means no valid subarray was found, so return 0. Otherwise, return min_length as the result.
"""

def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    # Example usage
    target1 = 7
    nums1 = [2,3,1,2,4,3]
    print(min_subarray_len(target1, nums1))  # Output: 2

    target2 = 4
    nums2 = [1,4,4]
    print(min_subarray_len(target2, nums2))  # Output: 1

    target3 = 11
    nums3 = [1,1,1,1,1,1,1,1]
    print(min_subarray_len(target3, nums3))  # Output: 0