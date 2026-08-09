# find largest and smallest elements in an array

def find_largest(arr: list[int]) -> int:
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

def find_smallest(arr: list[int]) -> int:
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

def main():
    print("Enter the number of elements in the array:")
    n = int(input())
    
    print(f"Enter {n} elements of the array (space-separated):")
    arr = list(map(int, input().split()))
    
    largest = find_largest(arr)
    smallest = find_smallest(arr)
    
    print(f"The largest element in the array is: {largest}")
    print(f"The smallest element in the array is: {smallest}")

if __name__ == "__main__":
    main()