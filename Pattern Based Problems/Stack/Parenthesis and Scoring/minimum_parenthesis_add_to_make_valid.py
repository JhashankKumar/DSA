# Minimum Add to Make Parentheses Valid
"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3
 
Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""

"""
Approach: Stack
1. Initialize a stack to keep track of unmatched parentheses.
2. Iterate through each character in the string:
   - If the character is '(', push it onto the stack.
   - If the character is ')':
     - If the stack is not empty and the top of the stack is '(', pop it (this means we found a matching pair).
     - If the stack is empty or the top of the stack is not '(', push ')' onto the stack (this means we have an unmatched closing parenthesis).
3. After processing all characters, the stack will contain unmatched parentheses.
4. The number of unmatched parentheses in the stack is the minimum number of moves required to make the string valid.
5. Return the size of the stack as the result.
"""

def min_add_to_make_valid(s: str) -> int:
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()  # Found a matching pair
            else:
                stack.append(char)  # Unmatched closing parenthesis
    
    return len(stack)  # The size of the stack is the number of unmatched parentheses

if __name__ == "__main__":
    # Test cases
    test_cases = [
        "())",
        "(((",
        "()",
        "(()))",
        "())(()",
        "((())",
        ")))((("
    ]
    
    for s in test_cases:
        print(f"Input: {s} => Output: {min_add_to_make_valid(s)}")