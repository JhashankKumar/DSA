# Move Zeros
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
"""

"""
Approach 1: Brute Force - O(n^2) Time and O(1) Space
1. Iterate through the array and whenever a 0 is found, remove it from the array and append it to the end of the array.
2. Return the modified array.
"""

from pyparsing import nums


def move_zeros_brute_force(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums

"""
Approach 2: Two Pointers - O(n) Time and O(1) Space
1. Initialize two pointers, left and right, both pointing to the start of the array.
2. Iterate through the array with the right pointer. If the element at the right pointer is not 0, swap the elements at the left and right pointers and increment both pointers. If the element at the right pointer is 0, just increment the right pointer.
3. Return the modified array.
"""

def move_zeros_two_pointers(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3, 4, 5],
        [0, 0, 0, 0],
        [1, 0, 2, 0, 3, 0],
    ]
    for nums in test_cases:
        print("Brute Force:", move_zeros_brute_force(nums))
        print("Two Pointers:", move_zeros_two_pointers(nums))