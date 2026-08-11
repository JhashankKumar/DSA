# arrange given array in ascending order and descending order

def main():
    print("Enter the elements of the array separated by spaces:")
    user_input = input()
    main_array = list(map(int, user_input.split()))
    ascending, descending = arrange_array(main_array)
    print("Original array:", main_array)
    print("Ascending order:", ascending)
    print("Descending order:", descending)


def arrange_array(arr):
    # Sort the array in ascending order
    ascending_order = sorted(arr)
    
    # Sort the array in descending order
    descending_order = sorted(arr, reverse=True)
    
    return ascending_order, descending_order

if __name__ == "__main__":
    main()