# Valid Parenthesis
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
Approach: Stack
1. Initialize an empty stack to keep track of opening brackets.
2. Create a mapping of closing brackets to their corresponding opening brackets.
3. Iterate through each character in the string:
   a. If the character is an opening bracket, push it onto the stack.
   b. If the character is a closing bracket, check if the stack is not empty and the top of the stack matches the corresponding opening bracket. If it does, pop the top of the stack. If it doesn't match or the stack is empty, return false.
4. After processing all characters, check if the stack is empty. If it is, return true (the string is valid). If not, return false (there are unmatched opening brackets).
"""

def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            return False  # Invalid character

    return len(stack) == 0  # Valid if no unmatched opening brackets remain

if __name__ == "__main__":
    # Example usage
    s1 = "()"
    print(is_valid(s1))  # Output: True

    s2 = "()[]{}"
    print(is_valid(s2))  # Output: True

    s3 = "(]"
    print(is_valid(s3))  # Output: False

    s4 = "([])"
    print(is_valid(s4))  # Output: True

    s5 = "([)]"
    print(is_valid(s5))  # Output: False