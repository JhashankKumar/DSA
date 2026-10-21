# Score of Parentheses
"""
Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2

Constraints:
2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

"""
Approach: Stack
1. Initialize an empty stack to keep track of scores.
2. Iterate through each character in the string:
   a. If the character is '(', push 0 onto the stack to represent a new score context.
   b. If the character is ')', pop the top score from the stack.
      - If the popped score is 0, it means we have a "()" pair, so we add 1 to the score of the previous context (if any).
      - If the popped score is greater than 0, it means we have a nested structure, so we add 2 times the popped score to the score of the previous context (if any).
3. After processing all characters, the final score will be the top of the stack (if any) or 0 if the stack is empty.
"""

def score_of_parentheses(s):
    stack = [0]  # Initialize stack with a base score of 0

    for char in s:
        if char == '(':
            stack.append(0)  # Start a new score context
        else:  # char == ')'
            score = stack.pop()  # Get the score of the current context
            if score == 0:
                stack[-1] += 1  # "()" contributes 1 to the previous context
            else:
                stack[-1] += 2 * score  # "(A)" contributes 2 * A to the previous context

    return stack.pop()  # The final score is the only element left in the stack

if __name__ == "__main__":
    # Example usage
    s1 = "()"
    print(score_of_parentheses(s1))  # Output: 1

    s2 = "(())"
    print(score_of_parentheses(s2))  # Output: 2

    s3 = "()()"
    print(score_of_parentheses(s3))  # Output: 2

    s4 = "(()(()))"
    print(score_of_parentheses(s4))  # Output: 6