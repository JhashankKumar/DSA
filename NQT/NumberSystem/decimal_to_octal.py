number1 = 45
octal = ""
# convert a decimal number to octal without using built-in functions
number1 = int(number1)
while number1 > 0:
    remainder = number1 % 8
    octal = str(remainder) + octal
    number1 //= 8
print(octal)  # Output: 55

# using built-in function
number1 = 45
octal = oct(number1)[2:]  # Convert decimal to octal and remove '0o'
print(octal)  # Output: 55