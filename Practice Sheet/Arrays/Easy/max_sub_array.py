# max subarray sum
"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.
"""

"""
Approach 1: Brute Force - O(n^2) Time and O(1) Space
The idea is to use two nested loops to find the sum of all possible subarrays 
and keep track of the maximum sum found so far. 
1. Initialize a variable max_sum to store the maximum sum found so far. Set it to a 
very small value (e.g., negative infinity).
2. Use two nested loops to iterate through all possible subarrays of the input array. 
The outer loop will fix the starting index of the subarray, and the inner loop will 
fix the ending index of the subarray.
3. For each subarray, calculate its sum and update max_sum if the current subarray sum 
is greater than max_sum.
4. After checking all possible subarrays, return max_sum as the result.
"""

def max_subarray_sum_brute_force(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    length = len(nums)
    
    # Iterate through all possible subarrays
    for i in range(length):
        current_sum = 0
        for j in range(i, length):
            current_sum += nums[j]  # Calculate the sum of the current subarray
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed
            
    return max_sum

"""
Approach 2: Kadane's Algorithm - O(n) Time and O(1) Space
The idea of Kadane's algorithm is to traverse over the array from left to right and for each element, 
find the maximum sum among all subarrays ending at that element. The result will be the maximum 
of all these values. 
To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use 
the maximum sum ending at the previous element.

So for any element, we have two choices:

Choice 1: Extend the maximum sum subarray ending at the previous element by adding 
the current element to it. If the maximum subarray sum ending at the previous index is positive, 
then it is always better to extend the subarray.
Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending 
at the previous index is negative, it is always better to start a new subarray from the current element.

This means that maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i]) 
and the maximum value of maxEnding at any index will be our answer.
"""

def max_subarray_sum_kadane(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0
    
    for num in nums:
        current_sum += num  # Add the current number to current_sum
        max_sum = max(max_sum, current_sum)  # Update max_sum if needed
        
        # If current_sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum (Brute Force):", max_subarray_sum_brute_force(arr))  # Output: 6

    print("Maximum subarray sum (Kadane's Algorithm):", max_subarray_sum_kadane(arr))  # Output: 6
