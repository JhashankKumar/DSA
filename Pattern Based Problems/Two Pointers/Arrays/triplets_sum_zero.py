# 3 Sum - Find All Triplets with Zero Sum
"""
Given an array arr[], the task is to find all possible indices {i, j, k} of triplet arr[i], arr[j], arr[k] such that their sum is equal to zero and all indices in a triplet should be distinct (i != j, j != k, k != i). We need to return indices of a triplet in sorted order, i.e., i < j < k.

Examples :

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation:  Two triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0

Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0

Input: arr[] = [2, 3, 1, 0, 5]
Output: []
Explanation: There is no triplet with sum 0.
"""

"""
Approach 1: Naive Approach - O(n^3) Time and O(1) Space
Three nested loops can be used to generate all possible triplets and check if their sum is equal to zero. If such a triplet is found, return the indices of the triplet. If no such triplet exists, return an empty list.
"""

def triplet_sum_zero_naive(arr):
    n = len(arr)
    result = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.append([i, j, k])
    return result





if __name__ == "__main__":
    test_cases = [
        ([0, -1, 2, -3, 1], [[0, 1, 4], [2, 3, 4]]),
        ([1, -2, 1, 0, 5], [[0, 1, 2]]),
        ([2, 3, 1, 0, 5], [])
    ]
    for arr, expected in test_cases:
        result = triplet_sum_zero_naive(arr)
        print(f"Input: {arr}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'Passed' if result == expected else 'Failed'}\n")  