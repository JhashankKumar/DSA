# Print subarray with maximum sum
"""
Given an array arr[], the task is to print the subarray having maximum sum.

Examples:

Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
Output: {7, -1, 2, 3}
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = {-2, -5, 6, -2, -3, 1, 5, -6}
Output: {6, -2, -3, 1, 5}
Explanation: The subarray {6, -2, -3, 1, 5} has the largest sum of 7.
"""

"""
Approach 1: Navive Approach - O(n^2) Time and O(1) Space
The idea is to run two nested loops to iterate over all possible subarrays and find the maximum sum. 
The outer loop will mark the starting point of a subarray and inner loop will mark the ending point 
of the subarray. At any time, if we find a subarray whose sum is greater than the maximum sum so far, 
then we will update the starting and ending point of the maximum sum subarray.
"""

def print_max_sum_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    start_index = 0
    end_index = 0
    
    # Iterate over all possible subarrays
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j
    
    # Print the subarray with maximum sum
    print("Subarray with maximum sum:", arr[start_index:end_index + 1])

"""
Approach 2: Kadane's Algorithm - O(n) Time and O(1) Space
The idea is similar to Kadane's Algorithm with the only difference that here, we need to keep track 
of the start and end of the subarray with maximum sum, that is the result array. Iterate over the 
array keeping track of the start and end of current subarray and at any point, if the sum of current 
subarray becomes greater than the result array, update the result array with the current subarray. 

For each element, we have two choices: 

Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current 
element to it. In this case, the ending index of the current subarray increases by 1.

Choice 2: Start a new subarray starting from the current element. In this case, the starting index 
of the current subarray updates to the current index.

If the maximum sum ending at an element becomes greater than the result array, we update the start 
and end of result subarray with the start and end of current subarray respectively.
"""

def print_max_sum_subarray_kadane(arr):
    n = len(arr)
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0
    start_index = 0
    end_index = 0
    temp_start_index = 0
    
    for i in range(n):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i
        
        if current_sum < 0:
            current_sum = 0
            temp_start_index = i + 1
    
    # Print the subarray with maximum sum
    print("Subarray with maximum sum:", arr[start_index:end_index + 1])

if __name__ == "__main__":
    arr1 = [2, 3, -8, 7, -1, 2, 3]
    print_max_sum_subarray(arr1)  # Output: [7, -1, 2, 3]
    print_max_sum_subarray_kadane(arr1)  # Output: [7, -1, 2, 3]

    arr2 = [-2, -5, 6, -2, -3, 1, 5, -6]
    print_max_sum_subarray(arr2)  # Output: [6, -2, -3, 1, 5]
    print_max_sum_subarray_kadane(arr2)  # Output: [6, -2, -3, 1, 5]