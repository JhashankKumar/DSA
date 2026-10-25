# Count occurrences of a number in a sorted array
"""
Given a sorted array arr[] and a number target, find the number of occurrences 
of target in given array. 

Examples:
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.

Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.

Constraints:
1 ≤ arr.size(), arr[i], target ≤ 106
"""

"""
Approach: Binary Search
1. We can use binary search to find the first and last occurrence of the target value in the sorted array.
2. We will implement two separate binary search functions: one for finding the first occurrence and another for finding the last occurrence.
3. The first occurrence function will continue searching in the left half of the array even after finding the target, while the last occurrence function will continue searching in the right half of the array after finding the target.
4. The number of occurrences of the target can be calculated as (last_position - first_position + 1).
5. If the target is not found, we will return 0.    
"""

def count_occurrences(arr, target):
    def find_first(arr, target):
        left, right = 0, len(arr) - 1
        first_position = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                first_position = mid
                right = mid - 1  # Continue searching in the left half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first_position

    def find_last(arr, target):
        left, right = 0, len(arr) - 1
        last_position = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                last_position = mid
                left = mid + 1  # Continue searching in the right half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last_position

    first_position = find_first(arr, target)
    last_position = find_last(arr, target)

    if first_position == -1 or last_position == -1:
        return 0
    
    return last_position - first_position + 1


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    print(count_occurrences(arr, target))  # Output: 4

    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 4
    print(count_occurrences(arr, target))  # Output: 0

    arr = [8, 9, 10, 12, 12, 12]
    target = 12
    print(count_occurrences(arr, target))  # Output: 3