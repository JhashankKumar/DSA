# finding average of numbers in an array using both inbuilt function and user defined function

def main():
    print("Enter the elements of the array separated by spaces:")
    user_input = input()
    main_array = list(map(int, user_input.split()))
    
    # Calculate average using inbuilt function
    inbuilt_average = sum(main_array) / len(main_array)
    
    # Calculate average using user-defined function
    user_defined_average = calculate_average(main_array)
    
    print("Original array:", main_array)
    print("Average using inbuilt function:", inbuilt_average)
    print("Average using user-defined function:", user_defined_average)


def calculate_average(arr: list[int]) -> float:
    total = 0
    for num in arr:
        total += num
    average = total / len(arr)
    return average

if __name__ == "__main__":
    main()