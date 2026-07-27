hexa_number = "2A"
decimal = 0
# convert a hexadecimal number to decimal without using built-in functions
hexa_number = hexa_number.upper()  # Ensure the hexadecimal number is in uppercase
for i in range(len(hexa_number)):
    if hexa_number[i].isdigit():
        decimal += int(hexa_number[i]) * (16 ** (len(hexa_number) - 1 - i))
    else:
        decimal += (ord(hexa_number[i]) - ord('A') + 10) * (16 ** (len(hexa_number) - 1 - i))
print(decimal)  # Output: 42

# using built-in function
hexa_number = "2A"
decimal = int(hexa_number, 16)  # Convert hexadecimal to decimal
print(decimal)  # Output: 42