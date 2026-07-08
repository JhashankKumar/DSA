def reverse_string(s):
    """
    Reverses the input string using a stack.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_str = ''
    
    # Pop all characters from the stack to get them in reverse order
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
string1 = "hello"
string2 = "world"
print(reverse_string(string1))  # Output: "olleh"
print(reverse_string(string2))  # Output: "dlrow"