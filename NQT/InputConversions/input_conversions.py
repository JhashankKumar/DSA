# convert a string to integer
number = "123"
integer_number = int(number)

# convert a string to float
float_number = float(number)

# convert a string to boolean
boolean_value = bool(int(number))  # Convert to int first, then to boolean

# convert a string to list
string_list = list(number)  # This will create a list of characters ['1', '2', '3']

# convert a string to tuple
tuple_value = tuple(number)  # This will create a tuple of characters ('1', '2', '3')

# convert a number to string
number_to_string = str(integer_number)

# convert a list to string
list_to_string = ''.join(string_list)  # This will create a string '123'

# convert a tuple to string
tuple_to_string = ''.join(tuple_value)  # This will create a string '123'

fruits = ["apple", "banana", "cherry"]

# convert a list to string with a separator
list_to_string_with_separator = ', '.join(fruits)  # This will create a string 'apple, banana, cherry'

student = {"name": "John", "age": 20}

print(list(student.keys()))
# ['name', 'age']

print(list(student.values()))
# ['John', 20]

print(list(student.items()))
# [('name', 'John'), ('age', 20)]

numbers = [1, 2, 2, 3]
print(set(numbers))  # {1, 2, 3}
print(tuple(numbers))  # (1, 2, 2, 3)


string_set = set("hello")
print(string_set)  # {'h', 'e', 'l', 'o'}

text = "hello world"
print(text.split())  # ['hello', 'world']

text_with_separator = "apple,banana,cherry"
print(text_with_separator.split(','))  # ['apple', 'banana', 'cherry']

print(text_with_separator.split())  # [apple,banana,cherry]  # This will not split as there is no whitespace

print(len(text_with_separator.split(',')))  # 3

print(len(text_with_separator.split()))  # 1