# Find the Median of Two Sorted Arrays
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

"""
Approach: Use Divide and Conquer
1. Merge the two sorted arrays nums1 and nums2 into a single sorted array.
2. Calculate the length of the merged array.
3. If the length is odd, return the middle element as the median.
4. If the length is even, return the average of the two middle elements as the median.
"""

def find_median_sorted_arrays(nums1, nums2):
    # Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    length = len(merged)

    # Calculate the median
    if length % 2 == 1:
        return float(merged[length // 2])
    else:
        mid1 = merged[length // 2 - 1]
        mid2 = merged[length // 2]
        return (mid1 + mid2) / 2.0

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(f"Median of {nums1} and {nums2} is: {find_median_sorted_arrays(nums1, nums2)}")  # Output: 2.0

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"Median of {nums1} and {nums2} is: {find_median_sorted_arrays(nums1, nums2)}")  # Output: 2.5