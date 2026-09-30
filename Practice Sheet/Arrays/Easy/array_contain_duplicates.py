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

"""
Approach 2: By using HashSet Data Structure – O(n) Time and O(n) Space

The main idea is to insert each value into a HashSet, which only stores unique elements. 
If any insertion fails or if any elements are already exits in HashSet, it means a duplicate exists, 
so return true. If all insertions succeed, it indicates that all elements are unique, so return false.

Time Complexity: O(n), As we are traversing over the array once.
Auxiliary space: O(n), As we are using unordered set which takes O(n) space in worst case, 
where n is the size of the array.
"""

def contains_duplicates_using_hashset(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


"""
Approach 3: By using Sorting – O(nlogn) Time and O(1) Space
The main idea is to first sort the array arr[] and then iterate through it to check if any 
adjacent elements are equal. If a pair of adjacent elements is equal, the function returns true, 
indicating the presence of duplicates. If no duplicates are found after traversing the entire array, 
the function returns false.

Time Complexity: O(n * logn), As we are using sorting function which takes nlogn time.
Auxiliary space: O(1), As we are not using extra space.
"""

def contains_duplicates_using_sorting(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return True
    return False


if __name__ == "__main__":
    arr1 = [4, 5, 6, 4]
    print(contains_duplicates(arr1))  # Output: True
    print(contains_duplicates_using_hashset(arr1))  # Output: True
    print(contains_duplicates_using_sorting(arr1))  # Output: True
    arr2 = [1, 2, 3, 4]
    print(contains_duplicates(arr2))  # Output: False
    print(contains_duplicates_using_hashset(arr2))  # Output: False
    print(contains_duplicates_using_sorting(arr2))  # Output: False