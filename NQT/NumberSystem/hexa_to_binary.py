hexa_number = "2A"
binary = ""
# convert a hexadecimal number to binary without using built-in functions
hexa_number = hexa_number.upper()  # Ensure the hexadecimal number is in uppercase
for digit in hexa_number:
    if digit.isdigit():
        decimal_value = int(digit)
    else:
        decimal_value = ord(digit) - ord('A') + 10
    binary_digit = ""
    for _ in range(4):
        binary_digit = str(decimal_value % 2) + binary_digit
        decimal_value //= 2
    binary += binary_digit
print(binary)  # Output: 101010

# using built-in function
hexa_number = "2A"
binary = bin(int(hexa_number, 16))[2:]  # Convert hexadecimal to binary and remove '0b'
print(binary)  # Output: 101010
