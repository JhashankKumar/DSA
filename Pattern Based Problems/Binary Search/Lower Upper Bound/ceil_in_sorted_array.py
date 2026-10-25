# Ceil in Sorted Array
"""
Given a sorted array arr[] (which may contain duplicate elements) and an integer x, 
find the 0-based index of the first element greater than or equal to x. 
This element is called the ceil of x.

If no such element exists, return -1.

Note: If multiple occurrences of the ceil exist, return the index of its first occurrence.

Examples:
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.

Input: arr[] = [1, 1, 2, 8, 10, 11, 12, 19], x = 0
Output: 0
Explanation: Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.

Constraints:
1 ≤ arr.size(), arr[i] ≤ 106
0 ≤ x ≤ 106
"""

"""
Approach: Binary Search
1. We can use binary search to find the ceil of x in the sorted array.
2. We will implement a binary search function that will continue searching in the left half of the array even after finding an element greater than or equal to x, to ensure we find the first occurrence.
3. If no such element exists, we will return -1.
"""

def ceil_in_sorted_array(arr, x):
    left, right = 0, len(arr) - 1
    ceil_index = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= x:
            ceil_index = mid
            right = mid - 1  # Continue searching in the left half
        else:
            left = mid + 1
            
    return ceil_index

if __name__ == "__main__":
    # Test cases
    print(ceil_in_sorted_array([1, 2, 8, 10, 11, 12, 19], 5))  # Output: 2
    print(ceil_in_sorted_array([1, 2, 8, 10, 11, 12, 19], 20)) # Output: -1
    print(ceil_in_sorted_array([1, 1, 2, 8, 10, 11, 12, 19], 0)) # Output: 0