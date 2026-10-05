# Triplet Sum in Array
"""
Given an array arr[] and an integer target, determine if there exists a triplet in the array 
whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false.

Examples: 

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
Output: true
Explanation: The triplet [1, 4, 8] sums up to 13

Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
Output: true
Explanation: The triplets [1, 3, 6] and [1, 2, 7] both sum to 10. 

Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24 
Output: false
Explanation:  No triplet in the array sums to 24.
"""

"""
Approach 1: Naive Approach - O(n^3) Time and O(1) Space
A simple method is to generate all possible triplets and compare the sum of every 
triplet with the given target. If the sum is equal to target, return true. Otherwise, return false.
"""

def triplet_sum_naive(arr, target):
    n = len(arr)
    print(n)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False

"""
Approach 2: Using Sorting and Two Pointers - O(n^2) Time and O(1) Space
1. Sort the array.
2. Iterate through the array, fixing one element at a time.
3. For the fixed element, use two pointers to find if there exists a pair in the remaining 
part of the array that sums to (target - fixed element).
4. If such a pair is found, return true. If the loop ends without finding any triplet, return false.

Let us understand with this example:
arr[] = [1, 4, 45, 6, 10, 8], target = 13

Sort the array: arr = [1, 4, 6, 8, 10, 45].
Set i = 0, fix the first element as 1, so the remaining two elements must sum to 12.
Initialize l = 1 (4) and r = 5 (45).
4 + 45 = 49, which is greater than 12, so move r left to reduce the sum.
4 + 10 = 14, which is still greater than 12, so move r left again.
4 + 8 = 12, which matches the required sum.
The triplet (1, 4, 8) adds up to 13, so the function returns true.
"""

def triplet_sum_two_pointers(arr, target):
    arr.sort()  # Sort the array first
    n = len(arr)
    
    for i in range(n - 2):
        # For each element, use two pointers to find a pair that sums to (target - arr[i])
        left, right = i + 1, n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1  # Move left pointer to the right to increase sum
            else:
                right -= 1  # Move right pointer to the left to decrease sum
                
    return False  # No triplet found that sums to target

if __name__ == "__main__":
    test_cases = [
        ([1, 4, 45, 6, 10, 8], 13),
        ([1, 2, 4, 3, 6, 7], 10),
        ([40, 20, 10, 3, 6, 7], 24),
        ([1, 2, 3], 6),
        ([1, -2, 1], 0),
        ([], 5),
        ([5], 5),
        ([1, 2], 3)
    ]
    
    for arr, target in test_cases:
        result_naive = triplet_sum_naive(arr, target)
        result_two_pointers = triplet_sum_two_pointers(arr, target)
        print(f"Does the array {arr} have a triplet that sums to {target}? {result_naive}")
        print(f"Using two pointers approach: {result_two_pointers}")