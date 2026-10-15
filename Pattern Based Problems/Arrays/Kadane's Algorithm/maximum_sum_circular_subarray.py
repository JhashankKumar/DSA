# Maximum Sum Circular Subarray Problem using Kadane's Algorithm

"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 
Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""

"""
Approach: Kadane's Algorithm for Maximum Sum Circular Subarray
1. Use Kadane's algorithm to find the maximum subarray sum in the non-circular case. This will give us the maximum sum of a subarray that does not wrap around the end of the array.
2. Calculate the total sum of the array.
3. Invert the sign of each element in the array and use Kadane's algorithm again to find the maximum subarray sum of the inverted array. This will give us the minimum subarray sum in the original array.
4. The maximum sum of a circular subarray can be obtained by subtracting the minimum subarray sum from the total sum of the array.
5. The final result will be the maximum of the non-circular maximum subarray sum and the circular maximum subarray sum
6. Handle the edge case where all elements are negative, in which case the maximum sum is the maximum element in the array.
"""

def max_subarray_sum_circular(nums):
    # Helper function to implement Kadane's algorithm
    def kadane(arr):
        max_so_far = arr[0]
        max_ending_here = arr[0]
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Step 1: Find the maximum subarray sum using Kadane's algorithm
    max_kadane = kadane(nums)

    # Step 2: Calculate the total sum of the array
    total_sum = sum(nums)

    # Step 3: Invert the sign of each element in the array and find the minimum subarray sum
    inverted_nums = [-num for num in nums]
    min_kadane = kadane(inverted_nums)

    # Step 4: Calculate the maximum circular subarray sum
    max_circular = total_sum + min_kadane  # This is equivalent to total_sum - (-min_kadane)

    # Step 5: Handle the edge case where all elements are negative
    if max_circular == 0:
        return max_kadane

    # Step 6: Return the maximum of non-circular and circular maximum subarray sums
    return max(max_kadane, max_circular)

if __name__ == "__main__":
    nums1 = [1, -2, 3, -2]
    print(max_subarray_sum_circular(nums1))  # Output: 3

    nums2 = [5, -3, 5]
    print(max_subarray_sum_circular(nums2))  # Output: 10

    nums3 = [-3, -2, -3]
    print(max_subarray_sum_circular(nums3))  # Output: -2