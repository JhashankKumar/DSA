# sub array with k distinct integers
"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: 
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: 
[1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""

"""
Approach 1: Sliding Window - O(n) Time and O(n) Space
1. Use a sliding window approach to maintain a window of elements with at most k distinct integers
2. Use a hash map to count the frequency of each integer in the current window
3. Expand the window by moving the right pointer and update the count of distinct integers
4. If the count of distinct integers exceeds k, shrink the window from the left until the count 
of distinct integers is at most k
5. Count the number of subarrays with exactly k distinct integers by calculating the number of 
subarrays with at most k distinct integers and subtracting the number of subarrays 
with at most (k-1) distinct integers
6. Return the count of subarrays with exactly k distinct integers
"""

def subarrays_with_k_distinct(nums, k):
    from collections import defaultdict

    def at_most_k_distinct(k):
        count = 0
        left = 0
        distinct = 0 
        freq = defaultdict(int)

        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            count += right - left + 1
        return count

    return at_most_k_distinct(k) - at_most_k_distinct(k - 1)

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 1, 2, 3], 2, 7),
        ([1, 2, 1, 3, 4], 3, 3),
        ([1, 2, 3, 4, 5], 5, 1),
        ([1, 1, 1, 1], 1, 10),
        ([1, 2, 3], 4, 0)
    ]
    for nums, k, expected in test_cases:
        result = subarrays_with_k_distinct(nums, k)
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'Passed' if result == expected else 'Failed'}\n")