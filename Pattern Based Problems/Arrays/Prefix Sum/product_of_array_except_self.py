# Product of Array Except Self
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""

"""
Approach: Prefix and Suffix Product - O(n) Time and O(1) Space
1. We can use two passes to calculate the product of all elements except self.
2. In the first pass, we can calculate the prefix product for each element and store it in the output array.
3. In the second pass, we can calculate the suffix product for each element and multiply it with the corresponding prefix product in the output array.
4. We can use a variable to keep track of the suffix product while iterating from the end of the array.
5. This way, we can achieve O(1) extra space complexity since we are using the output array to store the prefix products and a single variable for the suffix product.
"""

def product_except_self(nums):
    n = len(nums)
    output = [1] * n

    # Calculate prefix products
    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product *= nums[i]

    # Calculate suffix products and multiply with prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= nums[i]

    return output


if __name__ == "__main__":
    # Example usage:
    nums1 = [1, 2, 3, 4]
    print(product_except_self(nums1))  # Output: [24, 12, 8, 6]

    nums2 = [-1, 1, 0, -3, 3]
    print(product_except_self(nums2))  # Output: [0, 0, 9, 0, 0]