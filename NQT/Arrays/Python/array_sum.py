# find sum of array elements using both inbuilt function and user defined function

def main():
    print("Enter the elements of the array separated by spaces:")
    user_input = input()
    main_array = list(map(int, user_input.split()))
    
    # Calculate sum using inbuilt function
    inbuilt_sum = sum(main_array)
    
    # Calculate sum using user-defined function
    user_defined_sum = calculate_sum(main_array)
    
    print("Original array:", main_array)
    print("Sum using inbuilt function:", inbuilt_sum)
    print("Sum using user-defined function:", user_defined_sum)

def calculate_sum(arr: list[int]) -> int:
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    main()