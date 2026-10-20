# Make String Great
"""
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.
"""

"""
Approach: Stack Simulation
1. Initialize an empty stack to keep track of the characters in the string.
2. Iterate through each character in the string s.
   - If the stack is not empty and the top character of the stack and the current character are the same letter but in different cases 
   (one is lower-case and the other is upper-case), pop the top character from the stack (remove both characters).
   - Otherwise, push the current character onto the stack.
3. After processing all characters, the stack will contain the characters of the good string in order. 
Convert the stack to a string and return it. 
"""

def make_string_great(s):
    stack = []
    
    for char in s:
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:  # Check if the characters are the same letter in different cases
            stack.pop()  # Remove the top character from the stack
        else:
            stack.append(char)  # Add the current character to the stack
            
    return ''.join(stack)  # Convert the stack to a string and return it



if __name__ == "__main__":
    s1 = "leEeetcode"
    print(make_string_great(s1))  # Output: "leetcode"
    # print(make_string_great_using_string_methods(s1))  # Output: "leetcode"

    s2 = "abBAcC"
    print(make_string_great(s2))  # Output: ""
    # print(make_string_great_using_string_methods(s2))  # Output: ""

    s3 = "s"
    print(make_string_great(s3))  # Output: "s"
    # print(make_string_great_using_string_methods(s3))  # Output: "s"