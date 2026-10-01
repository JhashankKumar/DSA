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


"""
Approach 2: Using Binary Search twice - O(log n) Time and O(1) Space
1. The idea is to first find the pivot point in the rotated sorted array, 
which is the index of the largest element.
2. Once the pivot is found, we can perform binary search in the two subarrays 
divided by the pivot point. If the key is found in either of the subarrays, 
return the index; otherwise, return -1. 
3. This approach takes advantage of the fact that the array is sorted and rotated, 
allowing us to use binary search to efficiently locate the key.      
"""

def find_pivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = (low + high) // 2

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)

def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def search_in_rotated_sorted_array_two_pass(arr, key):
    n = len(arr)
    pivot = find_pivot(arr, 0, n - 1)

    if pivot == -1:
        return binary_search(arr, 0, n - 1, key)

    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot - 1, key)
    return binary_search(arr, pivot + 1, n - 1, key)

if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print(search_in_rotated_sorted_array_naive(arr, key))  # Output: 8
    print(search_in_rotated_sorted_array_two_pass(arr, key))  # Output: 8

    arr = [3, 5, 1, 2]
    key = 6
    print(search_in_rotated_sorted_array_naive(arr, key))  # Output: -1
    print(search_in_rotated_sorted_array_two_pass(arr, key))  # Output: -1

    arr = [33, 42, 72, 99]
    key = 42
    print(search_in_rotated_sorted_array_naive(arr, key))  # Output: 1
    print(search_in_rotated_sorted_array_two_pass(arr, key))  # Output: 1
