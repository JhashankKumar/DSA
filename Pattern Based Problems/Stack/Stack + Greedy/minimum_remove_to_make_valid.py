# Minimum Remove to Make Valid Parentheses
"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 
Constraints:
1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""
"""
Approach: Stack
1. Use a stack to keep track of the indices of the parentheses.
2. Iterate through each character in the string s:
   - If the character is '(', push its index onto the stack.
   - If the character is ')', check if the stack is not empty. If it is not empty, pop the top index from the stack (this means we have found a matching pair).
3. After processing all characters, the stack will contain the indices of unmatched '(' parentheses.
4. Create a set of indices to remove, which includes the indices in the stack and any unmatched ')' parentheses.
5. Construct the result string by including only the characters whose indices are not in the set of indices to remove.
6. Return the result string.
"""




def min_remove_to_make_valid(s: str) -> str:
    stack = []
    to_remove = set()

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)

    # Add remaining unmatched '(' indices to the set
    to_remove.update(stack)

    # Construct the result string
    result = []
    for i, char in enumerate(s):
        if i not in to_remove:
            result.append(char)

    return ''.join(result)

if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(min_remove_to_make_valid(s))  # Output: "lee(t(c)o)de"

    s = "a)b(c)d"
    print(min_remove_to_make_valid(s))  # Output: "ab(c)d"

    s = "))(("
    print(min_remove_to_make_valid(s))  # Output: ""