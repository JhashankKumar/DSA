# Find all anagrams in a string

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

"""
Approach: Sliding Window
1. Create a frequency map for the characters in string p.
2. Initialize two pointers, left and right, to the start of string s.
3. Expand the right pointer to include characters in the current window and update the frequency map accordingly
4. When the window size matches the length of p, check if the frequency map matches that of p. If it does, add the left pointer index to the result list.
5. Move the left pointer to shrink the window and update the frequency map accordingly.
6. Repeat steps 3-5 until the right pointer reaches the end of string s.
7. Return the result list containing the starting indices of all anagrams of p in s.
"""

def find_anagrams(s, p):
    from collections import Counter
    
    p_count = Counter(p)
    s_count = Counter()
    
    result = []
    left = 0
    
    for right in range(len(s)):
        s_count[s[right]] += 1
        
        if right - left + 1 == len(p):
            if s_count == p_count:
                result.append(left)
            
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
            
    return result

if __name__ == "__main__":
    s1, p1 = "cbaebabacd", "abc"
    print(find_anagrams(s1, p1))  # Output: [0, 6]

    s2, p2 = "abab", "ab"
    print(find_anagrams(s2, p2))  # Output: [0, 1, 2]