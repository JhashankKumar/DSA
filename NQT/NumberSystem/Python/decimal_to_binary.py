# convert a decimal number to binary without using built-in functions
decimal = 42
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print(binary)  # Output: 101010

# using built-in function
decimal = 42
binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b'
print(binary)  # Output: 101010