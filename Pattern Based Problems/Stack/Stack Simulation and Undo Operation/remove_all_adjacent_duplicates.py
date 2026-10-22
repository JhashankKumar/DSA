"""
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. 
It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""

"""
Approach: Stack Simulation
1. Initialize an empty stack to keep track of characters.
2. Iterate through each character in the string s.
3. For each character, check if the stack is not empty and the top of the stack is equal to the current character. If they are equal, pop the top character from the stack (this simulates removing the adjacent duplicates).
4. If they are not equal, push the current character onto the stack.
5. After processing all characters, the stack will contain the final string without adjacent duplicates. Convert the stack to a string and return it.
"""

def remove_adjacent_duplicates(s: str) -> str:
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the adjacent duplicate
        else:
            stack.append(char)  # Add the current character to the stack

    return ''.join(stack)  # Convert the stack back to a string

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("aabbcc", ""),
        ("abcde", "abcde"),
        ("aabbaa", ""),
        ("a", "a"),
        ("aa", ""),
        ("abccba", "")
    ]

    for s, expected in test_cases:
        result = remove_adjacent_duplicates(s)
        assert result == expected, f"Test failed for input: {s}. Expected: {expected}, Got: {result}"
    print("All tests passed!")