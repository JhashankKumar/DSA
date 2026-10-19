# Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.

"""

"""
Approach: Sliding Window
1. Initialize a set to store the characters in the current window and two pointers, left and right, to the start of the string.
2. Expand the right pointer to include characters in the current window and add them to the set.
3. If a duplicate character is found, move the left pointer to the right until the duplicate character is removed from the set.
4. Keep track of the maximum length of the substring without repeating characters during the process.
5. Repeat steps 2-4 until the right pointer reaches the end of the string.
6. Return the maximum length found.
"""

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
        
    return max_length

if __name__ == "__main__":
    s1 = "abcabcbb"
    print(length_of_longest_substring(s1))  # Output: 3

    s2 = "bbbbb"
    print(length_of_longest_substring(s2))  # Output: 1

    s3 = "pwwkew"
    print(length_of_longest_substring(s3))  # Output: 3