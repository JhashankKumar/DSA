# Next Greater Element II
"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] 
is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order 
next in the array, which means you could search circularly to find its next greater number. 
If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 
Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

"""
Approach:
1. Create a stack to keep track of the elements for which we are trying to find the next greater element.
2. Create a result list initialized with -1 for each element in nums.
3. Iterate through the array twice (to simulate the circular nature):
   a. For each element, while the stack is not empty and the current number is greater than the number at the index stored at the top of the stack, pop elements from the stack and update the result for those indices with the current number.
   b. Push the current index onto the stack.
4. Return the result list.
"""

def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n  # Initialize the result list with -1
    stack = []  # Stack to keep track of indices

    # Iterate through the array twice to simulate circular behavior
    for i in range(2 * n):
        current_index = i % n  # Get the current index in the circular array
        current_value = nums[current_index]

        # While stack is not empty and the current value is greater than the value at the index stored at the top of the stack
        while stack and nums[stack[-1]] < current_value:
            index = stack.pop()  # Pop the index from the stack
            result[index] = current_value  # Update the result for that index

        # Only push indices from the first pass (0 to n-1) onto the stack
        if i < n:
            stack.append(current_index)

    return result

if __name__ == "__main__":
    nums = [1, 2, 1]
    print(next_greater_elements(nums))  # Output: [2, -1, 2]

    nums = [1, 2, 3, 4, 3]
    print(next_greater_elements(nums))  # Output: [2, 3, 4, -1, 4]