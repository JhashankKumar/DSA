# find the maximum element in a sub-array of size k of a given array
def find_max_in_sub_array_of_size_k(arr: list[int], k: int) -> list[int]:
    if k <= 0 or k > len(arr):
        raise ValueError("Invalid sub-array size.")
    
    max_elements = []
    for i in range(len(arr) - k + 1):
        max_element = arr[i]
        for j in range(i, i + k):
            if arr[j] > max_element:
                max_element = arr[j]
        max_elements.append(max_element)
    return max_elements

# optimized version using deque for better performance
from collections import deque
def find_max_in_sub_array_of_size_k_optimized(arr: list[int], k: int) -> list[int]:
    if k <= 0 or k > len(arr):
        raise ValueError("Invalid sub-array size.")
    
    max_elements = []
    dq = deque()
    
    for i in range(len(arr)):
        # Remove elements not in the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove elements smaller than the current element from the deque
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # The first element of the deque is the largest element of the previous window
        if i >= k - 1:
            max_elements.append(arr[dq[0]])
    return max_elements

def main():
    print("Enter the number of elements in the array:")
    n = int(input())
    
    print(f"Enter {n} elements of the array (space-separated):")
    arr = list(map(int, input().split()))
    
    print("Enter the size of the sub-array (k):")
    k = int(input())
    
    try:
        max_elements = find_max_in_sub_array_of_size_k(arr, k)
        print(f"The maximum elements in each sub-array of size {k} are: {max_elements}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
