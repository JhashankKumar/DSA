# Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

"""
Approach 1: using Two Pointers - O(n) Time and O(1) Space
The idea is to use two pointers, one starting from the beginning of the string and the other starting from the end. 
We will move the pointers towards each other, skipping non-alphanumeric characters and comparing the characters at the pointers. 
If the characters are not equal, we return false. If the pointers meet or cross each other, we return true.    
"""
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters at left and right pointers
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("Not a palindrome", False)
    ]

    for s, expected in test_cases:
        result = is_palindrome(s)
        print(f"Input: {s}\nOutput: {result}\nExpected: {expected}\n{'Pass' if result == expected else 'Fail'}\n")