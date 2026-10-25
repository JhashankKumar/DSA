# Rotate an array by k elements
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 
Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

"""
Approach: Reverse Array
1. Reverse the entire array.
2. Reverse the first k elements.
3. Reverse the remaining n-k elements.
"""

def rotate(nums, k):
    n = len(nums)
    k %= n  # In case k is greater than n

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    rotate(nums1, k1)
    print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    k2 = 2
    rotate(nums2, k2)
    print(nums2)  # Output: [3, 99, -1, -100]