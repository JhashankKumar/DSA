def duplicate_parentheses(expression):
    stack = []
    for char in expression:
        if char == ')':
            top = stack.pop()
            elements_inside = 0
            while top != '(':
                elements_inside += 1
                top = stack.pop()
            if elements_inside < 1:
                return True
        else:
            stack.append(char)
    return False

# Example usage:
expression1 = "((a+b))"
expression2 = "(a+(b)/c)"
print(duplicate_parentheses(expression1))  # Output: True
print(duplicate_parentheses(expression2))  # Output: False
