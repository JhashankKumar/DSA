# Merge Sort using Divide and Conquer
"""
Given an array arr[], its starting position l and its ending position r. 
Sort the array using the merge sort algorithm.

Examples:
Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: We get the sorted array after using merge sort

Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: We get the sorted array after using merge sort 

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
"""

"""
Approach: Use Divide and Conquer
1. If the starting position l is less than the ending position r, find the middle position mid = (l + r) // 2.
2. Recursively sort the left half of the array from l to mid and the right half from mid + 1 to r.
3. Merge the two sorted halves using a helper function merge() that takes the array, starting position l, middle position mid, and ending position r as input.
4. The merge() function creates two temporary arrays to hold the left and right halves, and then merges them back into the original array in sorted order.
5. The final result is the sorted array after all recursive calls and merges are completed.
"""

def merge(arr, l, mid, r):
    # Create temporary arrays for left and right halves
    left_half = arr[l:mid + 1]
    right_half = arr[mid + 1:r + 1]

    # Initialize pointers for left_half, right_half, and the main array
    i = 0  # Pointer for left_half
    j = 0  # Pointer for right_half
    k = l  # Pointer for the main array

    # Merge the temporary arrays back into arr[l..r]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_half, if any
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_half, if any
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr

def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2  # Find the middle point
        merge_sort(arr, l, mid)  # Sort the first half
        merge_sort(arr, mid + 1, r)  # Sort the second half
        merge(arr, l, mid, r)  # Merge the sorted halves        

    return arr

if __name__ == "__main__":
    arr1 = [4, 1, 3, 9, 7]
    print(f"Sorted array: {merge_sort(arr1, 0, len(arr1) - 1)}")  # Output: [1, 3, 4, 7, 9]

    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Sorted array: {merge_sort(arr2, 0, len(arr2) - 1)}")  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]