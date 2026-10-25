# Floor In Sorted Array
"""
Given a sorted array arr[] and an integer x, 
find the index (0-based) of the largest element in arr[] that is less than or equal to x. 
This element is called the floor of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of floor of x, return the index of the last occurrence.

Examples
Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1.

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 11
Output: 4
Explanation: Largest Number less than or equal to 11 is 10, whose indices are 3 and 4. The index of last occurrence is 4.

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 0
Output: -1
Explanation: No element less than or equal to 0 is found. So, output is -1.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ x ≤ arr[n-1]
"""

"""
Approach: Binary Search
1. We can use binary search to find the floor of x in the sorted array.
2. We will implement a binary search function that will continue searching in the right half of the array even after finding an element less than or equal to x, to ensure we find the last occurrence.
3. If no such element exists, we will return -1.
"""

def floor_in_sorted_array(arr, x):
    left, right = 0, len(arr) - 1
    floor_index = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= x:
            floor_index = mid
            left = mid + 1  # Continue searching in the right half
        else:
            right = mid - 1
            
    return floor_index

if __name__ == "__main__":
    # Test cases
    print(floor_in_sorted_array([1, 2, 8, 10, 10, 12, 19], 5))  # Output: 1
    print(floor_in_sorted_array([1, 2, 8, 10, 10, 12, 19], 11)) # Output: 4
    print(floor_in_sorted_array([1, 2, 8, 10, 10, 12, 19], 0))  # Output: -1
    