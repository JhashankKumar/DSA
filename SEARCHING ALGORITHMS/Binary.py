# Binary search algorithm
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid  # return the index if target is found
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # return -1 if target is not found

# input from user
n = int(input("Enter the number of elements in the list: "))
# create an empty list
my_list = []
# loop to get the elements from user
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

# input the target value to search for
target = int(input("Enter the target value to search for: "))

# call the binary search function
result = binary_search(my_list, target)
# output the result
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in the list.")