# Binary Search
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

"""
Approach: Binary Search
1. Initialize two pointers, left and right, to the start and end of the array respectively
2. While left is less than or equal to right:
   - Calculate the middle index mid as (left + right) // 2
   - If nums[mid] is equal to target, return mid (the index of the target)
   - If nums[mid] is less than target, move the left pointer to mid + 1 (search in the right half)
   - If nums[mid] is greater than target, move the right pointer to mid - 1 (search in the left half)
3. If the target is not found, return -1
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(nums, target))  # Output: 4

    target = 2
    print(binary_search(nums, target))  # Output: -1