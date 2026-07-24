# binary to hexadecimal without using built-in functions
binary = "101010"
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
hexadecimal = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
    decimal //= 16
print(hexadecimal)  # Output: 2A

# using built-in function
binary = "101010"
hexadecimal = hex(int(binary, 2))[2:].upper()
# Convert binary to decimal, then to hexadecimal and remove '0x' prefix, convert to uppercase
print(hexadecimal)  # Output: 2A