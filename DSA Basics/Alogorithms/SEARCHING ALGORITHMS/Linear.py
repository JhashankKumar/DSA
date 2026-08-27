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

# linear search algorithm
def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index  # return the index if target is found
    return -1  # return -1 if target is not found

# call the linear search function
result = linear_search(my_list, target)
# output the result
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in the list.")