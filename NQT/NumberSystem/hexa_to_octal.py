hexa_number = "2A"
octal = ""
# convert a hexadecimal number to octal without using built-in functions
hexa_number = hexa_number.upper()  # Ensure the hexadecimal number is in uppercase
# Step 1: Convert hexadecimal to decimal
decimal = 0
for i in range(len(hexa_number)):
    if hexa_number[i].isdigit():
        decimal += int(hexa_number[i]) * (16 ** (len(hexa_number) - 1 - i))
    else:
        decimal += (ord(hexa_number[i]) - ord('A') + 10) * (16 ** (len(hexa_number) - 1 - i))
# Step 2: Convert decimal to octal
while decimal > 0:
    remainder = decimal % 8
    octal = str(remainder) + octal
    decimal //= 8
print(octal)  # Output: 52

# using built-in function
hexa_number = "2A"
octal = oct(int(hexa_number, 16))[2:]  
# Convert hexadecimal to decimal, then to octal and remove '0o' prefix
print(octal)  # Output: 52