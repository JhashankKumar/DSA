# Valid Parentheses in an Expression
"""
Given a string s containing three types of brackets {}, () and []. Determine whether the Expression are balanced or not.
An expression is balanced if each opening bracket has a corresponding closing bracket of the same type, the pairs are properly ordered and no bracket closes before its matching opening bracket.

-> Balanced: "[()()]{}" → every opening bracket is closed in the correct order.
-> Not balanced: "([{]})" → the ']' closes before the matching '{' is closed, breaking the nesting rule.
Example: 

Input: s = "[{()}]"
Output: true
Explanation:  All the brackets are well-formed.

Input:  s = "([{]})"
Output: false
Explanation: The expression is not balanced because there is a closing ']' before the closing '}'.
"""
"""
Approach 1 : Using Stack - O(n) Time and O(n) Space
We use a stack to ensure that every opening has a matching closing. Each opening is pushed onto the stack. 
When a closing appears, we check if the stack has a corresponding opening to pop; if not, the string is unbalanced. 
After processing the entire string, the stack must be empty for it to be considered balanced.
"""
def valid_parentheses_stack(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False
    return not stack


if __name__ == "__main__":
    test_cases = ["[{()}]", "([{]})", "[()()]{}", "((()))", "{[()()]}", "({[)]}", "((())", "(()))", "", "[]{}()"]
    for s in test_cases:
        result = valid_parentheses_stack(s)
        print(f"Is the expression '{s}' balanced? {result}")