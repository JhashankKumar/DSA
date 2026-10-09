# Max Consecutive Ones III
"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

"""
Approach: Sliding Window - O(n) Time and O(1) Space
1. Initialize two pointers, left and right, to the start of the array.
2. Initialize a variable max_count to keep track of the maximum number of consecutive 1's found so far.
3. Initialize a variable zero_count to keep track of the number of 0's in the current window.
4. Iterate through the array using the right pointer:
   a. If nums[right] is 0, increment zero_count.
   b. While zero_count exceeds k, move the left pointer to the right and decrement zero_count if nums[left] is 0.
   c. Update max_count with the size of the current window (right - left + 1) if it is greater than max_count.
5. Return max_count after the loop ends.
"""
