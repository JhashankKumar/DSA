# Back Space String Compare
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""

"""
Approach: Stack Simulation
1. Initialize two empty stacks for both strings s and t.
2. Iterate through each character in string s:
   - If the character is not '#', push it onto the stack.
   - If the character is '#', pop the top character from the stack if it's not empty.
3. Repeat the same process for string t.
4. After processing both strings, compare the contents of both stacks.
5. If the stacks are equal, return true; otherwise, return false.
"""

def backspace_compare(s, t):
    def build_stack(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return stack
    
    return build_stack(s) == build_stack(t)


if __name__ == "__main__":
    s1 = "ab#c"
    t1 = "ad#c"
    print(backspace_compare(s1, t1))  # Output: True

    s2 = "ab##"
    t2 = "c#d#"
    print(backspace_compare(s2, t2))  # Output: True

    s3 = "a#c"
    t3 = "b"
    print(backspace_compare(s3, t3))  # Output: False

    # Test the two-pointer approach
    # print(backspace_compare_two_pointers(s1, t1))  # Output: True
    # print(backspace_compare_two_pointers(s2, t2))  # Output: True
    # print(backspace_compare_two_pointers(s3, t3))  # Output: False