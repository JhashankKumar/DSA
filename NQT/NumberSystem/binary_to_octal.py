# Converting binary to octal without using built-in functions
binary = "101010"
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
octal = 0
place = 1
while decimal > 0:
    octal += (decimal % 8) * place
    decimal //= 8
    place *= 10
print(octal)  # Output: 52

# using built-in function
binary = "101010"
octal = oct(int(binary, 2))[2:]  # Convert binary to decimal, then to octal and remove '0o' prefix
print(octal)  # Output: 52