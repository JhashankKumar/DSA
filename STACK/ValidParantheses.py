def valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            print(f"Stack after popping '{top_element}': {stack}")  # Debug statement to show stack state
            if mapping[char] != top_element:
                return False
        else:
            if char in mapping.values():
                stack.append(char)
            print(f"Stack after pushing '{char}': {stack}")  # Debug statement to show stack state
    
    return not stack

# Example usage:
expression1 = "((a+b))"
expression2 = "(a+(b)/c)"
expression3 = "((a+b)"
expression4 = "(a+b))"
print(valid_parentheses(expression1))  # Output: True
print(valid_parentheses(expression2))  # Output: True
print(valid_parentheses(expression3))  # Output: False
print(valid_parentheses(expression4))  # Output: False