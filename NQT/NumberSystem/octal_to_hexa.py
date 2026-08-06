# octal to hexadecimal conversion without using built-in functions
def octal_to_decimal(octal_num):
    decimal_num = 0
    power = 0
    while octal_num > 0:
        digit = octal_num % 10
        decimal_num += digit * (8 ** power)
        octal_num //= 10
        power += 1
    return decimal_num

def decimal_to_hexadecimal(decimal_num):
    if decimal_num == 0:
        return "0"
    hex_num = ""
    hex_chars = "0123456789ABCDEF"
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_num = hex_chars[remainder] + hex_num
        decimal_num //= 16
    return hex_num

def octal_to_hexadecimal(octal_num):
    decimal_num = octal_to_decimal(octal_num)
    return decimal_to_hexadecimal(decimal_num)

def main():
    octal_num = int(input("Enter an octal number: "))
    hex_num = octal_to_hexadecimal(octal_num)
    print(f"The hexadecimal equivalent of octal {octal_num} is: {hex_num}")

if __name__ == "__main__":
    main()