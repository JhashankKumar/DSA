octal_number = "52"
# octal to decimal conversion without using built-in functions
decimal_number = 0
# Reverse the octal number to process from least significant digit
octal_number_reversed = octal_number[::-1]
for index, digit in enumerate(octal_number_reversed):
    decimal_number += int(digit) * (8 ** index)
print(f"The decimal equivalent of octal {octal_number} is {decimal_number}.")

# octal to decimal conversion using built-in functions
octal_number = "52"
decimal_number = int(octal_number, 8)
print(f"The decimal equivalent of octal {octal_number} using built-in function is {decimal_number}.")