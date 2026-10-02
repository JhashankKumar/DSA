# Check if two Strings are Anagrams of each other
"""
Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams - i.e., if they contain the same characters with the same frequencies.

Examples:

Input: s1 = "geeks"  s2 = "kseeg"
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergyy"
Output: false
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.
"""

"""
Approach 1 : Sorting and Comparison - O(n log n + m log m) Time and O(n+m) Space
The idea is that if the strings are anagrams, then their characters will be the same, just rearranged.  

We sort the characters in both strings, the sorted strings will be identical if the original strings were anagrams.
"""

def is_anagram_sorting(s1, s2):
    # Sort both strings and compare
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"

    result_sorting = is_anagram_sorting(s1, s2)
    print(f"Are '{s1}' and '{s2}' anagrams (using sorting)? {result_sorting}")