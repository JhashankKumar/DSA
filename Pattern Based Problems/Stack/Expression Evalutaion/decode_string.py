# Decode String
"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed to be 
a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data 
does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 
Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

"""
Approach: Stack based solution (Two Stack Approach)
1. Initialize two stacks: one for numbers (num_stack) and one for strings (str_stack).
2. Initialize a current string (current_str) and a current number (current_num)
3. Iterate through each character in the input string:
   a. If the character is a digit, build the current number.
   b. If the character is '[', push the current number onto num_stack and the current string onto str_stack, then reset current_num and current_str.
   c. If the character is ']', pop a number from num_stack and a string from str_stack, then repeat the current_str that many times and append it to the popped string, and set this as the new current_str.
   d. If the character is a letter, append it to current_str.
4. After processing all characters, the current_str will contain the decoded string.
"""

def decode_string(s):
    num_stack = []  # Stack to keep track of numbers
    str_stack = []  # Stack to keep track of strings
    current_str = ""  # Current string being built
    current_num = 0  # Current number being built

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)  # Build the current number
        elif char == '[':
            num_stack.append(current_num)  # Push the current number onto the stack
            str_stack.append(current_str)  # Push the current string onto the stack
            current_num = 0  # Reset current number
            current_str = ""  # Reset current string
        elif char == ']':
            repeat_times = num_stack.pop()  # Pop the number of times to repeat
            prev_str = str_stack.pop()  # Pop the previous string
            current_str = prev_str + current_str * repeat_times  # Build the new string
        else:
            current_str += char  # Append character to the current string

    return current_str  # Return the final decoded string

if __name__ == "__main__":
    s = "3[a]2[bc]"
    print(decode_string(s))  # Output: "aaabcbc"

    s = "3[a2[c]]"
    print(decode_string(s))  # Output: "accaccacc"

    s = "2[abc]3[cd]ef"
    print(decode_string(s))  # Output: "abcabccdcdcdef"