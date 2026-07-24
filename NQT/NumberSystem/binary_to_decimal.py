# Converting binary to decimal without using built-in functions
binary = "101010"
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
print(decimal)  # Output: 42

# using built-in function
binary = "101010"
decimal = int(binary, 2)
print(decimal)  # Output: 42