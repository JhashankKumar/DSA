# Triplet Sum in Array
"""
Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false.

Examples: 

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
Output: true
Explanation: The triplet [1, 4, 8] sums up to 13

Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
Output: true
Explanation: The triplets [1, 3, 6] and [1, 2, 7] both sum to 10. 

Input: arr[] = [40, 20, 10, 3, 6, 7], sum = 24 
Output: false
Explanation:  No triplet in the array sums to 24.
"""

"""
Approach 1: Naive Approach - O(n^3) Time and O(1) Space
A simple method is to generate all possible triplets and compare the sum of every triplet with the given target. If the sum is equal to target, return true. Otherwise, return false.
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
        result = triplet_sum_naive(arr, target)
        print(f"Does the array {arr} have a triplet that sums to {target}? {result}")