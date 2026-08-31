"""
Given an array of integers arr[], the task is to find the maximum and minimum elements 
in the array using the minimum number of comparisons.

Examples:

Input: arr[] = [3, 5, 4, 1, 9]
Output: [1, 9]
Explanation: The minimum element is 1, and the maximum element is 9.

Input: arr[] = [22, 14, 8, 17, 35, 3]
Output: [3, 35] 
Explanation: The minimum element is 3, and the maximum element is 35.
"""

"""
Approach 1:

[Naive Approach] By Sorting the array - O(n log n) Time and O(1) Space
The idea is to firstly sort the array in ascending order.
Once the array is sorted, the first element of the array will be the minimum element and the 
last element of the array will be the maximum element.

Number of Comparisons
The number of comparisons is equal to the number of comparisons made during the sorting process. 
For any comparison-based sorting algorithm, the minimum number of comparisons required in the 
worst case to sort an array of n elements is O(n log n). Hence, the number of comparisons made 
in this approach is O(n log n).
"""

def min_max_sorting(arr):
    # Sort the array
    arr.sort()
    
    # The first element is the minimum and the last element is the maximum
    return [arr[0], arr[-1]]

"""
Approach 2:

[Better Approach I] Iterating the array - O(n) Time and O(1) Space

"""

def min_max_iterating(arr):
    # Initialize min and max with the first element of the array
    min_elem = arr[0]
    max_elem = arr[0]
    
    # Iterate through the array to find min and max
    for num in arr:
        if num < min_elem:
            min_elem = num
        elif num > max_elem:
            max_elem = num
            
    return [min_elem, max_elem]


if __name__ == "__main__":
    # Test cases
    arr1 = [3, 5, 4, 1, 9]
    print(min_max_sorting(arr1))  # Output: [1, 9]
    print(min_max_iterating(arr1))  # Output: [1, 9]

    arr2 = [22, 14, 8, 17, 35, 3]
    print(min_max_sorting(arr2))  # Output: [3, 35]
    print(min_max_iterating(arr2))  # Output: [3, 35]