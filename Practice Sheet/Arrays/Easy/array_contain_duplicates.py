# Check if array contains duplicates
"""
Given an integer array arr[], check if the array contains any duplicate value.

Examples:

Input: arr[] = {4, 5, 6, 4}
Output: true
Explanation: 4 is the duplicate value.

Input: arr[] = {1, 2, 3, 4}
Output: false
Explanation: All values are distinct.
"""

"""
Approach 1: Naive - O(n^2) Time and O(1) Space
The simple idea is to use a nested loop to compare each element in the array with every other element.
If any two elements are found to be the same, return true, indicating the array has a duplicate element. 
If no duplicates are found after all comparisons, return false.

Time Complexity: O(N2), As we are using nested loop over the given array, where N is the number of 
elements in the given array.
Auxiliary Space: O(1), As we are not using any extra space.
"""

def contains_duplicates(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False




if __name__ == "__main__":
    arr1 = [4, 5, 6, 4]
    print(contains_duplicates(arr1))  # Output: True

    arr2 = [1, 2, 3, 4]
    print(contains_duplicates(arr2))  # Output: False