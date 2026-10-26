# Next Greater Element I
"""
The next greater element of some element x in an array is the first greater element 
that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a 
subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater 
element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""

"""
Algorithm:
1. Create a stack to keep track of the elements for which we are trying to find the next greater element.
2. Create a dictionary to store the next greater element for each number in nums2.
3. Iterate through nums2 in reverse order:
   a. While the stack is not empty and the current number is greater than or equal to the number at the top of the stack, pop elements from the stack.
   b. If the stack is not empty after the above step, the next greater element for the current number is the number at the top of the stack. Otherwise, it is -1.
   c. Store the next greater element in the dictionary.
   d. Push the current number onto the stack.
4. Iterate through nums1 and use the dictionary to find the next greater element for each number in nums1, and store the results in an output list.
5. Return the output list.
"""

def next_greater_element(nums1, nums2):
    # Step 1: Create a stack and a dictionary to store the next greater elements
    stack = []
    next_greater = {}

    # Step 2: Iterate through nums2 in reverse order
    for num in reversed(nums2):
        # Step 3a: Pop elements from the stack while they are less than or equal to the current number
        while stack and stack[-1] <= num:
            stack.pop()
        
        # Step 3b: Determine the next greater element
        if stack:
            next_greater[num] = stack[-1]
        else:
            next_greater[num] = -1
        
        # Step 3d: Push the current number onto the stack
        stack.append(num)

    # Step 4: Create the output list for nums1 using the next greater elements dictionary
    result = [next_greater[num] for num in nums1]

    # Step 5: Return the result
    return result


if __name__ == "__main__":
    # Example usage
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(next_greater_element(nums1, nums2))  # Output: [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(next_greater_element(nums1, nums2))  # Output: [3, -1]