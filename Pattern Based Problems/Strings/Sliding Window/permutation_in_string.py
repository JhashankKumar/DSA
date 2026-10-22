# Permutation in String
"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

"""
Approach: Sliding Window
1. Create a frequency map for the characters in s1.
2. Initialize two pointers, left and right, to represent the current window in s2.
3. Expand the right pointer to include characters in the window and update the frequency map accordingly.
4. If the window size exceeds the length of s1, move the left pointer to shrink the window and update the frequency map.
5. At each step, check if the frequency map of the current window matches the frequency map of s1. If it does, return true.
6. If the right pointer reaches the end of s2 and no permutation is found, return false.
"""

def check_inclusion(s1: str, s2: str) -> bool:
    from collections import Counter

    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        return False

    s1_count = Counter(s1)
    window_count = Counter()

    for i in range(len_s2):
        window_count[s2[i]] += 1

        if i >= len_s1:
            left_char = s2[i - len_s1]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1

        if window_count == s1_count:
            return True

    return False

if __name__ == "__main__":
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
        ("hello", "ooolleoooleh", False),
        ("a", "a", True),
        ("abc", "bbbca", True)
    ]
    
    for s1, s2, expected in test_cases:
        result = check_inclusion(s1, s2)
        print(f"Input: s1 = {s1}, s2 = {s2}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")