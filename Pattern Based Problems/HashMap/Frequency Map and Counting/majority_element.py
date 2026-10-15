# Majority Element Problem
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
"""

"""
Approach: Using a HashMap to find the majority element
1. Create a HashMap to store the frequency of each element in the array.
2. Iterate through the array and update the frequency of each element in the HashMap.
3. After populating the HashMap, iterate through the HashMap to find the element with the maximum frequency.
4. Return the element with the maximum frequency as the majority element.
"""
def majority_element(nums):
    # Step 1: Create a HashMap to store the frequency of each element
    frequency_map = {}
    
    # Step 2: Iterate through the array and update the frequency of each element
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    # Step 3: Find the element with the maximum frequency
    majority_count = len(nums) // 2
    for num, count in frequency_map.items():
        if count > majority_count:
            return num

if __name__ == "__main__":
    # Example usage
    nums1 = [3, 2, 3]
    print(majority_element(nums1))  # Output: 3

    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element(nums2))  # Output: 2