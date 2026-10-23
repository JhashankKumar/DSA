# Valid Palindrome II
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""

"""
Approach: Use Two Pointers - O(n) Time and O(1) Space
1. We can use two pointers, one starting from the beginning of the string and the other starting from the end.
2. We will move the pointers towards each other, comparing the characters at the pointers.
3. If the characters are not equal, we can either skip the character at the left pointer or the character at the right pointer and check if the remaining substring is a palindrome.
4. If the characters are equal, we continue moving the pointers towards each other.
5. If the pointers meet or cross each other, we return true.
6. If we reach the end of the string without finding a mismatch, we return true.
7. If we find a mismatch and neither of the substrings formed by skipping one character is a palindrome, we return false.
"""

def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Check if skipping the left character or the right character results in a palindrome
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    # Example usage:
    s1 = "aba"
    print(valid_palindrome(s1))  # Output: True

    s2 = "abca"
    print(valid_palindrome(s2))  # Output: True

    s3 = "abc"
    print(valid_palindrome(s3))  # Output: False