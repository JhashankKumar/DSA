# Maximum Product Subarray Problem using Kadane's Algorithm

"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

​​​​​​​Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

"""
Approach: Kadane's Algorithm for Maximum Product Subarray
1. Initialize two variables, max_so_far and min_so_far, to the first element of the array. 
These will keep track of the maximum and minimum products ending at the current position.
2. Initialize a variable, result, to the first element of the array. This will store the maximum product found so far.
3. Iterate through the array starting from the second element.
4. For each element, if it is negative, swap max_so_far and min_so_far. This is because multiplying by a negative number 
will turn the maximum product into a minimum product and vice versa.
5. Update max_so_far to be the maximum of the current element and the product of max_so_far and the current element.
6. Update min_so_far to be the minimum of the current element and the product of min_so_far and the current element.
7. Update result to be the maximum of result and max_so_far.
8. Return result as the final answer, which represents the largest product of the contiguous subarray.  
"""

def max_product(nums):
    # Initialize max_so_far and min_so_far to the first element of the array
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is negative, swap max_so_far and min_so_far
        if nums[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        # Update max_so_far and min_so_far
        max_so_far = max(nums[i], max_so_far * nums[i])
        min_so_far = min(nums[i], min_so_far * nums[i])

        # Update result to be the maximum of result and max_so_far
        result = max(result, max_so_far)

    return result