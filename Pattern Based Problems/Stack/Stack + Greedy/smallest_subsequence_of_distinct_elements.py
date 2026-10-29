# Smallest Subsequence of Distinct Elements

"""
Given a string s, return the lexicographically smallest subsequence of s that 
contains all the distinct characters of s exactly once.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

"""
Approach: Stack
1. Use a stack to build the result string.
2. Use a set to keep track of the characters that are already in the stack.
3. Iterate through each character in the string s:
   - If the character is already in the stack, skip it.
   - While the stack is not empty, and the current character is smaller than the top character of the stack, and the top character appears later in the string, pop the top character from the stack and remove it from the set.
   - Push the current character onto the stack and add it to the set.
4. Join the characters in the stack to form the result string.
"""

def smallest_subsequence(s: str) -> str:
    stack = []
    seen = set()
    last_occurrence = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
        if c in seen:
            continue
        while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
            seen.remove(stack.pop())
        stack.append(c)
        seen.add(c)

    return ''.join(stack)

if __name__ == "__main__":
    s = "bcabc"
    print(smallest_subsequence(s))  # Output: "abc"

    s = "cbacdcbc"
    print(smallest_subsequence(s))  # Output: "acdb"