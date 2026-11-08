# Binary Search Algorithm
"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

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
Approach: Use Divide and Conquer
1. Initialize two pointers, left and right, to the start and end of the array, respectively.
2. While left is less than or equal to right, calculate the middle index mid = (left + right) // 2.
3. If nums[mid] is equal to the target, return mid.
4. If nums[mid] is less than the target, move the left pointer to mid + 1 to search in the right half of the array.
5. If nums[mid] is greater than the target, move the right pointer to mid - 1 to search in the left half of the array.
6. If the target is not found, return -1.
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
    nums1, target1 = [-1, 0, 3, 5, 9, 12], 9
    print(f"Index of {target1} in {nums1} is: {binary_search(nums1, target1)}")  # Output: 4

    nums2, target2 = [-1, 0, 3, 5, 9, 12], 2
    print(f"Index of {target2} in {nums2} is: {binary_search(nums2, target2)}")  # Output: -1