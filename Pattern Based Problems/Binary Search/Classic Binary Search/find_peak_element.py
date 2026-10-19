# Find the peak element in an array
"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered 
to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.
 
Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

"""
Approach: Modified Binary Search
1. Initialize two pointers, left and right, to the start and end of the array respectively
2. While left is less than right:
   - Calculate the middle index mid as (left + right) // 2
   - If nums[mid] is less than nums[mid + 1], it means the peak element is in the right half, so move the left pointer to mid + 1
   - Otherwise, it means the peak element is in the left half or at mid, so move the right pointer to mid
3. When left equals right, the peak element is found at index left (or right)
"""

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return left

if __name__ == "__main__":
    nums1 = [1,2,3,1]
    print(find_peak_element(nums1))  # Output: 2

    nums2 = [1,2,1,3,5,6,4]
    print(find_peak_element(nums2))  # Output: 5