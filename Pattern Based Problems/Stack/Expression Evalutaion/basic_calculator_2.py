# Basic Calculator II
"""
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

"""
Approach: Stack based solution
1. Initialize a stack to keep track of numbers and a variable to keep track of the current number and the last operator.
2. Iterate through the string character by character.
3. If the character is a digit, build the current number.
4. If the character is an operator or the end of the string is reached, process the last operator:
   a. If the last operator was '+', push the current number onto the stack.
   b. If the last operator was '-', push the negative of the current number onto the stack.
   c. If the last operator was '*', pop the top of the stack, multiply it by the current number, and push the result back onto the stack.
   d. If the last operator was '/', pop the top of the stack, divide it by the current number (truncating toward zero), and push the result back onto the stack.
5. Reset the current number and update the last operator to the current character.
6. After processing all characters, sum up all the numbers in the stack to get the final result.   
"""

def calculate(s):
    stack = []
    current_number = 0
    last_operator = '+'
    
    for i, char in enumerate(s):
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        
        if char in "+-*/" or i == len(s) - 1:
            if last_operator == '+':
                stack.append(current_number)
            elif last_operator == '-':
                stack.append(-current_number)
            elif last_operator == '*':
                stack.append(stack.pop() * current_number)
            elif last_operator == '/':
                top = stack.pop()
                if top < 0:
                    stack.append(-(-top // current_number))
                else:
                    stack.append(top // current_number)
            
            current_number = 0
            last_operator = char
    
    return sum(stack)

if __name__ == "__main__":
    s = "3+2*2"
    print(calculate(s))  # Output: 7

    s = " 3/2 "
    print(calculate(s))  # Output: 1

    s = " 3+5 / 2 "
    print(calculate(s))  # Output: 5