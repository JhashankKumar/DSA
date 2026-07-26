decimal = "42"
hexa = ""
# convert a decimal number to hexadecimal without using built-in functions
decimal = int(decimal)
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexa = str(remainder) + hexa
    else:
        hexa = chr(remainder - 10 + ord('A')) + hexa
    decimal //= 16
print(hexa)  # Output: 2A

# using built-in function
decimal = 42
hexa = hex(decimal)[2:].upper()  
# Convert decimal to hexadecimal and remove '0x', then convert to uppercase
print(hexa)  # Output: 2A