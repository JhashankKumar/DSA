# Basic Calculator I
"""
Given a string s representing a valid expression, 
implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates 
strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 
Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

"""
Approach: Stack
1. Initialize a stack to keep track of the signs and results.
2. Iterate through the string character by character.
3. If the character is a digit, build the current number.
4. If the character is a '+' or '-', update the result with the current number and reset the current number.
5. If the character is '(', push the current result and sign onto the stack, and reset the result and sign.
6. If the character is ')', pop the sign and result from the stack, and update the result with the current number.
7. At the end of the iteration, add the last number to the result.
"""

def calculate(s):
    stack = []
    current_number = 0
    result = 0
    sign = 1  # 1 means positive, -1 means negative

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in '+-':
            result += sign * current_number
            current_number = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * current_number
            current_number = 0
            result *= stack.pop()  # pop the sign
            result += stack.pop()   # pop the previous result

    result += sign * current_number
    return result

"""
Approach 2: Using In-built eval() function (Not allowed as per the problem statement)
"""
def calculate_with_eval(s):
    return eval(s)
    
if __name__ == "__main__":
    # Test cases
    s1 = "1 + 1"
    print(calculate(s1))  # Output: 2
    print(calculate_with_eval(s1))  # Output: 2

    s2 = " 2-1 + 2 "
    print(calculate(s2))  # Output: 3
    print(calculate_with_eval(s2))  # Output: 3

    s3 = "(1+(4+5+2)-3)+(6+8)"
    print(calculate(s3))  # Output: 23
    print(calculate_with_eval(s3))  # Output: 23