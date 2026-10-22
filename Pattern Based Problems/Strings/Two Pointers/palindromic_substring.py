# Palindromic Substring
"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def expand_around_center(s: str, left: int, right: int) -> int:
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

def count_palindromic_substrings(s: str) -> int:
    total_count = 0
    
    for i in range(len(s)):
        total_count += expand_around_center(s, i, i)      # Odd length palindromes
        total_count += expand_around_center(s, i, i + 1)  # Even length palindromes
        
    return total_count


if __name__ == "__main__":
    # Test cases
    test_cases = [
        "abc",
        "aaa",
        "racecar",
        "abccba",
        "aabb"
    ]
    
    for s in test_cases:
        print(f"Input: {s} => Output: {count_palindromic_substrings(s)}")