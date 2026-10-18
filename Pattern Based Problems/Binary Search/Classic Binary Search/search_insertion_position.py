# Search Insertion Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

"""
Approach: Binary Search
1. Initialize two pointers, left and right, to 0 and len(nums) - 1 respectively
2. While left is less than or equal to right:
   - Calculate the middle index mid as (left + right) // 2
   - If nums[mid] is equal to target, return mid (the index of the target)
   - If nums[mid] is less than target, move the left pointer to mid + 1 (search in the right half)
   - If nums[mid] is greater than target, move the right pointer to mid - 1 (search in the left half)
3. If the target is not found, return left (the index where the target would be inserted in order)
"""

def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(search_insert(nums, target))  # Output: 2

    target = 2
    print(search_insert(nums, target))  # Output: 1

    target = 7
    print(search_insert(nums, target))  # Output: 4