# Longest Palindromic Substring
"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""
Approach: Two Pointers
1. Initialize two pointers, left and right, to the start and end of the string respectively
2. While left is less than right, check if the characters at the left and right pointers are equal
3. If they are equal, move the left pointer to the right and the right pointer to the left, and continue checking
4. If they are not equal, move the left pointer to the right and reset the right pointer to the end of the string
5. Keep track of the longest palindromic substring found so far
6. Return the longest palindromic substring after checking all possible substrings
"""

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindromic_substring(s: str) -> str:
    if len(s) < 1:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)      # Odd length palindromes
        len2 = expand_around_center(s, i, i + 1)  # Even length palindromes
        max_len = max(len1, len2)
        
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "racecar",
        "noon",
        "abcde",
        "abccba",
        "abcdedcba"
    ]
    
    for s in test_cases:
        result = longest_palindromic_substring(s)
        print(f"Input: {s} => Longest Palindromic Substring: {result}")