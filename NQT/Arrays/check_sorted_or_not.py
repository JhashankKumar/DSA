# check the given array is sorted or not in ascending order and descending order seperately

def check_ascending_order(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def check_descending_order(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True

def main():
    print("Enter the number of elements in the array:")
    n = int(input())
    
    print(f"Enter {n} elements of the array (space-separated):")
    arr = list(map(int, input().split()))
    
    if check_ascending_order(arr):
        print("The array is sorted in ascending order.")
    elif check_descending_order(arr):
        print("The array is sorted in descending order.")
    else:
        print("The array is not sorted.")

if __name__ == "__main__":
    main()