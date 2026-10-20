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


"""
Methods to check if two characters are the same letter in different cases:
1. Using ASCII values: Check if the absolute difference between the ASCII values of the two characters is 32. This works because the ASCII value of a lower-case letter is 32 greater than its corresponding upper-case letter.
2. Using string methods: Convert both characters to the same case (either lower or upper) and compare them. If they are equal, then they are the same letter in different cases.
3. Using a set of pairs: Create a set of pairs of lower-case and upper-case letters. Check if the two characters form a pair in the set. If they do, then they are the same letter in different cases.
4. Using a dictionary: Create a dictionary that maps each lower-case letter to its corresponding upper-case letter and vice versa. Check if the two characters are in the dictionary and if they map to each other. If they do, then they are the same letter in different cases.
5. Using regular expressions: Use a regular expression to check if the two characters match the pattern of a lower-case letter followed by its corresponding upper-case letter or vice versa. If they match the pattern, then they are the same letter in different cases.
"""

"""
Approach 2: Using string methods + stack
1. Initialize an empty stack to keep track of the characters in the string.
2. Iterate through each character in the string s.
   - If the stack is not empty and the top character of the stack and the current character are the same letter in different cases (one is lower-case and the other is upper-case), pop the top character from the stack (remove both characters).
   - Otherwise, push the current character onto the stack.
3. After processing all characters, the stack will contain the characters of the good string in order. Convert the stack to a string and return it. 
"""

def make_string_great_using_string_methods(s):
    stack = []
    
    for char in s:
        if stack and stack[-1].lower() == char.lower() and stack[-1] != char:  # Check if the characters are the same letter in different cases
            stack.pop()  # Remove the top character from the stack
        else:
            stack.append(char)  # Add the current character to the stack
            
    return ''.join(stack)  # Convert the stack to a string and return it


if __name__ == "__main__":
    s1 = "leEeetcode"
    print(make_string_great(s1))  # Output: "leetcode"
    print(make_string_great_using_string_methods(s1))  # Output: "leetcode"

    s2 = "abBAcC"
    print(make_string_great(s2))  # Output: ""
    print(make_string_great_using_string_methods(s2))  # Output: ""

    s3 = "s"
    print(make_string_great(s3))  # Output: "s"
    print(make_string_great_using_string_methods(s3))  # Output: "s"