# Find first and last position of an element in a sorted array
"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

"""
Approach: Binary Search
1. We can use binary search to find the first and last occurrence of the target value in the sorted array.
2. We will implement two separate binary search functions: one for finding the first occurrence and another for finding the last occurrence.
3. The first occurrence function will continue searching in the left half of the array even after finding the target, while the last occurrence function will continue searching in the right half of the array after finding the target.
4. If the target is not found, we will return [-1, -1].
5. The overall time complexity of this approach is O(log n)
"""

def find_first_last_position(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first_position = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                first_position = mid
                right = mid - 1  # Continue searching in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first_position

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last_position = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                last_position = mid
                left = mid + 1  # Continue searching in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last_position

    first_pos = find_first(nums, target)
    last_pos = find_last(nums, target)
    
    return [first_pos, last_pos]


# Example usage:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(find_first_last_position(nums1, target1))  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(find_first_last_position(nums2, target2))  # Output: [-1, -1]