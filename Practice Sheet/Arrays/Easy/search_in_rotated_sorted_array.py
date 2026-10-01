# Search in Rotated Sorted Array
"""
Given a sorted and rotated array arr[] of distinct elements, find the index of 
given key in the array. If the key is not present in the array, return -1.

Examples:  

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is present at index 8.

Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: 6 is not present.

Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1
"""

"""
Approach 1: Naive - O(n) Time and O(1) Space
A simple approach is to iterate through the array and check for each element, 
if it matches the target then return the index, otherwise return -1. 
To know more about the implementation refer Linear Search Algorithm.
"""

def search_in_rotated_sorted_array_naive(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print(search_in_rotated_sorted_array_naive(arr, key))  # Output: 8

    arr = [3, 5, 1, 2]
    key = 6
    print(search_in_rotated_sorted_array_naive(arr, key))  # Output: -1

    arr = [33, 42, 72, 99]
    key = 42
    print(search_in_rotated_sorted_array_naive(arr, key))  # Output: 1
