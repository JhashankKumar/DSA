# aaabbbccc  -> 3a3b3c

def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append(f"{count}{prev_char}")
            print(f"Compressed so far: {''.join(compressed)}")  # Debugging statement
            prev_char = char
            count = 1

    compressed.append(f"{count}{prev_char}")  # Append the last group
    print(compressed)
    
    return ''.join(compressed)

# input from user
input_string = input("Enter a string to compress: ")
# call the compress_string function
compressed_string = compress_string(input_string)
# output the result
print(f"Compressed string: {compressed_string}")