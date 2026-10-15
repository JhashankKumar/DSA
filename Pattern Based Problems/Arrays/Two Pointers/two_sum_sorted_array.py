# Two Sum II - Input Array Is Sorted

"""
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

Find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of 
length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

"""
Intuition💡
Because the input array is already sorted, we can avoid a brute-force approach or 
utilizing extra space (like a hash map) by taking advantage of the array's ascending order. 
A two-pointer approach starting from both ends of the array allows us to efficiently narrow down 
our search for the target sum.

Approach🎯
Initialize two pointers: left at the beginning (index 0) and right at the end of the array.

In a loop, check the sum of the elements at these two pointers (numbers[left]+numbers[right]).

If the sum exactly matches the target, we've found our answer. Since the problem requires 1-based 
indexing, return [left+1,right+1].

If the sum is greater than the target, we need a smaller sum. Since the array is sorted, 
we can decrease our sum by moving the right pointer one step to the left.

If the sum is less than the target, we need a larger sum. We can increase our sum by moving 
the left pointer one step to the right.

Repeat this process until the pointers meet.

Complexity⌛
Time complexity: O(n)
We traverse the array at most once, where n is the number of elements in the array.

Space complexity: O(1)
We only use two integer variables (left and right) for the pointers, which requires 
constant extra space.
"""

def two_sum_sorted_array(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1  # Move left pointer to the right to increase sum
        else:
            right -= 1  # Move right pointer to the left to decrease sum
    
    return []  # In case there is no solution, though the problem guarantees one

if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
        ([1, 2, 3, 4, 4], 8),
        ([1, 2, 3, 4, 5], 10)
    ]
    
    for numbers, target in test_cases:
        result = two_sum_sorted_array(numbers, target)
        print(f"Input: numbers = {numbers}, target = {target} => Output: {result}")