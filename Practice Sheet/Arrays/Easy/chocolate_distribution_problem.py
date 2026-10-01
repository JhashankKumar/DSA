# Chocolate Distribution Problem
"""
Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. 
Each packet can have a variable number of chocolates. There are m students, 
the task is to distribute chocolate packets such that: 

Each student gets exactly one packet.
The difference between the maximum and minimum number of chocolates in the packets 
given to the students is minimized.

Examples:

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
Output: 2 
Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, 
that is 2. 

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5 
Output: 7
Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will get the minimum difference, 
that is 9 - 2 = 7. 
"""

"""
Approach 1: Naive - O(n^2) Time and O(1) Space
The idea is to generate all subsets of size m of arr[]. For every subset, find the difference 
between the maximum and minimum elements in it. Finally, return the minimum difference.
"""
def chocolate_distribution_naive(arr, m):
    n = len(arr)
    if m == 0 or n == 0:
        return 0

    if n < m:
        return -1

    min_diff = float('inf')

    # Generate all subsets of size m
    from itertools import combinations
    for subset in combinations(arr, m):
        current_diff = max(subset) - min(subset)
        min_diff = min(min_diff, current_diff)

    return min_diff

"""
Approach 2: Sliding Window Technique - O(nlogn) Time and O(1) Space
The idea is to first sort the array, then use sliding window technique to choose consecutive 
elements to minimize the difference. After sorting the array, the difference between the 
maximum and minimum values in any window of size m is minimized. 
"""

def chocolate_distribution(arr, m):
    n = len(arr)
    if m == 0 or n == 0:
        return 0

    if n < m:
        return -1

    arr.sort()
    min_diff = float('inf')

    for i in range(n - m + 1):
        current_diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, current_diff)

    return min_diff

if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    print(chocolate_distribution(arr, m))  # Output: 2
    print(chocolate_distribution_naive(arr, m))  # Output: 2

    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 5
    print(chocolate_distribution(arr, m))  # Output: 7
    print(chocolate_distribution_naive(arr, m))  # Output: 7