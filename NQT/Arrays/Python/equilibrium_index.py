"""
Given an array arr[] of size n, find an equilibrium index (if any) or -1 if no equilibrium index 
exists. The equilibrium index of an array is an index such that the sum of all elements at lower 
indexes equals the sum of all elements at higher indexes. When the index is at the start of the 
array, the left sum is 0, and when it's at the end, the right sum is 0.

Note: If multiple equilibrium indices exist, return the first one encountered from left to right.
Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum on the left of index 2 is 1 + 2 = 3 and sum on the right of index 2 is 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1 
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum on the left of index 3 is -7 + 1 + 5 = -1 and sum 
on the right of index 3 is -4 + 3 + 0 = -1.
"""

"""
Approach:
1. [Naive Approach] Using Nested Loop - O(n2) Time and O(1) Space
2. [Optimized Approach] Using Prefix Sum and suffix Sum - O(n) Time and O(1) Space
"""

def equilibrium_index_loop_method(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            return i
    return -1

def equilibrium_index_prefix_sum_method(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]  # Now total_sum is the right sum for index i

        if left_sum == total_sum:
            return i

        left_sum += arr[i]

    return -1


def main():
    arr1 = [1, 2, 0, 3]
    arr2 = [1, 1, 1, 1]
    arr3 = [-7, 1, 5, 2, -4, 3, 0]

    print("Using Loop Method:")
    print(f"Equilibrium index of {arr1} is: {equilibrium_index_loop_method(arr1)}")
    print(f"Equilibrium index of {arr2} is: {equilibrium_index_loop_method(arr2)}")
    print(f"Equilibrium index of {arr3} is: {equilibrium_index_loop_method(arr3)}")

    print("\nUsing Prefix Sum Method:")
    print(f"Equilibrium index of {arr1} is: {equilibrium_index_prefix_sum_method(arr1)}")
    print(f"Equilibrium index of {arr2} is: {equilibrium_index_prefix_sum_method(arr2)}")
    print(f"Equilibrium index of {arr3} is: {equilibrium_index_prefix_sum_method(arr3)}")

if __name__ == "__main__":
    main()