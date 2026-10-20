"""
You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, 
you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.
Note that the string concatenates after removing the substring and could produce 
new "AB" or "CD" substrings.

Example 1:
Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.

Example 2:
Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.

Constraints:

1 <= s.length <= 100
s consists only of uppercase English letters.
"""

"""
Approach: Stack Simulation
1. Initialize an empty stack.
2. Iterate through each character in the string s:
   - If the stack is not empty and the top of the stack along with the current character forms either "AB" or "CD", pop the top character from the stack (removing the substring).
   - Otherwise, push the current character onto the stack.
3. After processing all characters, the stack will contain the remaining characters of the string.
4. The minimum possible length of the resulting string is the size of the stack.
"""

def minimum_length_after_removing_substring(s):
    stack = []
    for char in s:
        if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
            stack.pop()  # Remove the substring "AB" or "CD"
        else:
            stack.append(char)  # Push the current character onto the stack
    return len(stack)  # The size of the stack is the minimum possible length


if __name__ == "__main__":
    # Test cases
    print(minimum_length_after_removing_substring("ABFCACDB"))  # Output: 2
    print(minimum_length_after_removing_substring("ACBBD"))     # Output: 5
    print(minimum_length_after_removing_substring("ABCDABCD"))  # Output: 0
    print(minimum_length_after_removing_substring("AABBCCDD"))  # Output: 0
    print(minimum_length_after_removing_substring("XYZ"))       # Output: 3