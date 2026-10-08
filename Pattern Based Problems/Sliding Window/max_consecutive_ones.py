# Max Consecutive Ones
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

"""
Approach: Sliding Window - O(n) Time and O(1) Space
1. Initialize two pointers, left and right, to the start of the array.
2. Initialize a variable max_count to keep track of the maximum number of consecutive 1's found so far.
3. Iterate through the array using the right pointer:
   a. If nums[right] is 1, increment the current count of consecutive 1's.
   b. If nums[right] is 0, reset the current count of consecutive 1's to 0.
   c. Update max_count if the current count of consecutive 1's is greater than max_count.
4. Return max_count after the loop ends.
"""

def find_max_consecutive_ones(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count