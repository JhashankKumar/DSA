# move all zeros to the end of an array
"""
example:
Input: [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
Output: [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
"""

def move_zeros_to_end(arr: list[int]) -> list[int]:
    non_zero_index = 0  # Index to place the next non-zero element

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    # Fill the remaining positions with zeros
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr

def main():
    print("Enter the number of elements in the array:")
    n = int(input())
    
    print(f"Enter {n} elements of the array (space-separated):")
    arr = list(map(int, input().split()))
    
    result = move_zeros_to_end(arr)
    print(f"The array after moving all zeros to the end is: {result}")

if __name__ == "__main__":
    main()