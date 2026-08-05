octal_number = "52"
binary = ""
# convert an octal number to binary without using built-in functions
octal_number = int(octal_number)
while octal_number > 0:
    remainder = octal_number % 2
    binary = str(remainder) + binary
    octal_number //= 2
print(binary)  # Output: 101010

# using built-in function
octal_number = "52"
binary = bin(int(octal_number, 8))[2:]  
# Convert octal to decimal, then to binary and remove '0b' prefix
print(binary)  # Output: 101010