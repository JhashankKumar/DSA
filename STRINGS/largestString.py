# lexicographically largest string in a list of strings

def largest_string(s):
    if not s:
        return ""

    largest = s[0]
    for char in s[1:]:
        # print(f"Comparing {char} with {largest}")  # Debugging statement
        if char > largest:
            largest = char

    return largest

# lexicographically smallest string in a list of strings

def smallest_string(s):
    if not s:
        return ""

    smallest = s[0]
    for char in s[1:]:
        # print(f"Comparing {char} with {smallest}")  # Debugging statement
        if char < smallest:
            smallest = char

    return smallest


# list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# find the lexicographically largest fruit
largest_fruit = largest_string(fruits)
smallest_fruit = smallest_string(fruits)
# output the result
print(f"The lexicographically largest fruit is: {largest_fruit}")
print(f"The lexicographically smallest fruit is: {smallest_fruit}")


# sort the list of fruits in lexicographical order
sorted_fruits = sorted(fruits, reverse=True)
# output the sorted list
print(f"The sorted list of fruits is: {sorted_fruits}")


# algorithm to sort a list of strings in lexicographical order
def sort_strings(string_list):
    if not string_list:
        return []

    sorted_list = []
    while string_list:
        largest = max(string_list)
        sorted_list.append(largest)
        string_list.remove(largest)

    return sorted_list

# algorithm to sort a list of strings in lexicographical reverse order 
def sort_strings_reverse(string_list):
    if not string_list:
        return []

    sorted_list = []
    while string_list:
        smallest = min(string_list)
        sorted_list.append(smallest)
        string_list.remove(smallest)

    return sorted_list

# algorithm to sort a list of strings in lexicographical reverse order using built-in sort
def sort_strings_reverse_builtin(string_list):
    return sorted(string_list, reverse=True)