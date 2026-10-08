# Sort an array of 0s, 1s and 2s - Dutch National Flag Problem
"""
Given an array arr[] consisting of only 0s, 1s, and 2s. The objective is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.

This problem is the same as the famous "Dutch National Flag problem". The problem was proposed by Edsger Dijkstra. The problem is as follows:

Given n balls of colour red, white or blue arranged in a line in random order. You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, with the order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: [0, 0, 1, 1, 2, 2] has all 0s first, then all 1s and all 2s in last.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
"""

"""
Approach 1: Naive Approach - O(nlogn) Time and O(1) Space
1. Sort the array using any sorting algorithm.
2. Return the sorted array.
"""

def sort_colors_naive(arr):
    arr.sort()
    return arr


"""
Approach 2: Using Counting - O(n) Time and O(1) Space
1. Count the number of 0s, 1s and 2s in the array.
2. Overwrite the original array with the counted number of 0s, 1s and 2s.
3. Return the sorted array.

Time Complexity: O(2 × n), where n is the number of elements in the array
Auxiliary Space: O(1)

The issues with this approach are:

It would not work if 0s and 1s represent keys of objects.
Not stable
Requires two traversals
"""

def sort_colors_counting(arr):
    count_0 = count_1 = count_2 = 0
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    index = 0
    for _ in range(count_0):
        arr[index] = 0
        index += 1
    for _ in range(count_1):
        arr[index] = 1
        index += 1
    for _ in range(count_2):
        arr[index] = 2
        index += 1

    return arr


if __name__ == "__main__":
    test_cases = [
        ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),
        ([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2])
    ]

    # user input 
    # arr = list(map(int, input("Enter the array elements (0s, 1s, 2s) separated by space: ").strip().split()))
    for arr, expected in test_cases:
        naive_result = sort_colors_naive(arr)
        counting_result = sort_colors_counting(arr.copy())

        print(f"Input: {arr}")
        print(f"Expected: {expected}")
        print(f"Result (Naive): {naive_result}")
        print(f"Result (Counting): {counting_result}") 